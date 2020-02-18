#CODE4---To extract for drug data for the main drug table----
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

#------------CODE4----------------
#Part executing for drug interaction
outFileName3 = OUTPUT_PATH + "drugInteraction.csv"

df3 = df.select(df['drugbank-id']['_VALUE'][0],df['drug-interactions']['drug-interaction']['drugbank-id'],df['drug-interactions']['drug-interaction']['name'],\
	df['drug-interactions']['drug-interaction']['description'])
df4 = df3.toPandas().dropna(thresh=2,subset=('drug-interactions.drug-interaction.drugbank-id','drug-interactions.drug-interaction.name','drug-interactions.drug-interaction.description'))
df4 = sqlContext.createDataFrame(df4)
#df4.show()


#function to split array value into seperate row
def tripleExplode(ar):
	rowDict = ar.asDict()
	
	aList = rowDict.pop('drug-interactions.drug-interaction.drugbank-id')
	bList = rowDict.pop('drug-interactions.drug-interaction.name')
	cList = rowDict.pop('drug-interactions.drug-interaction.description')
	
  
	for a,b,c in zip(aList,bList,cList):
		newDict = dict(rowDict)
		
		newDict['drug-interactions.drug-interaction.drugbank-id'] = a
		newDict['drug-interactions.drug-interaction.name'] = b
		newDict['drug-interactions.drug-interaction.description'] = c
		yield Row(**newDict)

df_split2 = sqlContext.createDataFrame(df4.rdd.flatMap(tripleExplode))

df_split2.show()
df_split2.toPandas().to_csv(outFileName3,sep='\t', index=False,encoding='utf-8')
