#CODE6---To extract for drug data for the main drug table----
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

#--------CODE6---------------
#code to seperate out the dosages file
outFileName5 = OUTPUT_PATH + "drugDosages.csv"

df8 = df.select(df['drugbank-id']['_VALUE'][0],df['dosages']['dosage'])

df8 = df8.toPandas().dropna()
df9 = sqlContext.createDataFrame(df8)
df9.show()

def singleExplode(ar):
	rowDict = ar.asDict()
	
	aList = rowDict.pop("dosages.dosage")
	for a in zip(aList):
		newDict = dict(rowDict)
		newDict['Dosages'] = a
		yield Row(**newDict)


df_split4 = sqlContext.createDataFrame(df9.rdd.flatMap(singleExplode))
df_split4.show()
df_split4.printSchema()
df_split4 = df_split4.toPandas()
df_split4 = df_split4.join(pd.DataFrame(df_split4["Dosages"].apply(pd.Series)))
df_split4 = df_split4.join(pd.DataFrame(df_split4[0].values.tolist(), columns=['FORM','ROUTE','STRENGTH'])).drop(['Dosages',0],axis=1)
df_split5 = df_split4.dropna()
df_split5['STRENGTH'] = df_split5["STRENGTH"].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
df_split5.to_csv(outFileName5,sep='\t', index=False,encoding='utf-8')
print(df_split5.columns)