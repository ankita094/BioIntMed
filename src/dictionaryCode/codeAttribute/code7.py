#CODE7---To extract for drug data for the main drug table----
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

#-------------CODE7----------------
# code to seperate out the category file
outFileName5 = OUTPUT_PATH + "drugCategory.csv"

df9 = df.select(df['drugbank-id']['_VALUE'][0],df['categories']['category'])

df9 = df9.toPandas().dropna()
df9 = sqlContext.createDataFrame(df9)
df9.show()

def singleExplode(ar):
	rowDict = ar.asDict()
	
	aList = rowDict.pop("categories.category")
	for a in zip(aList):
		newDict = dict(rowDict)
		newDict['category'] = a
		yield Row(**newDict)



df_split6 = sqlContext.createDataFrame(df9.rdd.flatMap(singleExplode))
df_split6.show()
df_split6.printSchema()
df_split6 = df_split6.toPandas()
df_split6 = df_split6.join(pd.DataFrame(df_split6["category"].apply(pd.Series)))
df_split6 = df_split6.join(pd.DataFrame(df_split6[0].values.tolist(), columns=['CATEGORY','MESH_ID'])).drop(['category',0],axis=1)
df_split6.to_csv(outFileName5,sep='\t', index=False,encoding='utf-8')
print(df_split5.columns)