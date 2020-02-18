#CODE9---To extract for drug data for the main drug table----
#Spark version 2.3.1

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
import json
from pyspark.sql.types import StructType
import re
from pyspark.sql.functions import UserDefinedFunction
import pyspark.sql.functions as fun
from pyspark.sql.functions import Column,udf,lit
import pandas as pd
from pyspark.sql import Row
import itertools
from itertools import zip_longest
from collections import defaultdict
from functools import reduce
from pyspark.sql.functions import udf, explode, first
from pyspark.sql.functions import collect_list


config = SparkConf().setAll([('spark.master','local[4]'),('spark.executor.memory', '10g'), ('spark.executor.cores', '6'), ('spark.cores.max', '6'), ('spark.driver.memory','10g'),("spark.driver.maxResultSize",'3g')])
scc = SparkContext(conf=config)
sqlContext = SQLContext(scc)

#INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/fulldatabase.xml" 
INPUT_PATH = 'sampleData/dictionaryExample/DrugbankExampleData.xml'
OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/" 

df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='drug').load(INPUT_PATH)
#df = df.limit(1000)
df.printSchema()


#--------------CODE9-------------
#Extract gene part

outFileName6 = OUTPUT_PATH + "drugTarget.csv"

df12 = df.select(df['drugbank-id']['_VALUE'][0],df['targets'])
df12.printSchema()

df12.printSchema()


df13 = df12.select('`drugbank-id._VALUE[0]`','targets.target.actions.action','targets.target.id','targets.target.name','targets.target.organism',\
	"`targets`.`target`.`polypeptide`.`_id`")
	
df13.show(10,False)

#function to split array value into seperate row
def pentaExplode(ar):
	rowDict = ar.asDict()
	
	aList = rowDict.pop('targets.target.id')
	bList = rowDict.pop('targets.target.name')
	cList = rowDict.pop('targets.target.organism')
	dList = rowDict.pop('targets.target.actions.action')
	eList = rowDict.pop('targets.target.polypeptide')
	for a,b,c,d,e in zip(aList,bList,cList,dList,eList):
		newDict = dict(rowDict)
		
		newDict['targets.target.id'] = a
		newDict['targets.target.name'] = b
		newDict['targets.target.organism'] = c
		newDict['targets.target.actions.action'] = d
		newDict['targets.target.polypeptide'] = e
		yield Row(**newDict)

df_split8 = sqlContext.createDataFrame(df12.rdd.flatMap(pentaExplode))



df_split8.show()
df_split8.toPandas().to_csv(outFileName6,sep='\t', index=False,encoding='utf-8')


