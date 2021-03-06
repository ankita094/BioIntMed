#CODE5---To extract for drug data for the main drug table----
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

#---------------CODE5------------------
#For preparing the data for synonyms of drug
outFileName4 = OUTPUT_PATH + "drugSynonym1.csv"

df6 = df.select(df['drugbank-id']['_VALUE'][0],df['synonyms']['synonym']['_VALUE'])
df7 = df6.toPandas().dropna()
df7 = sqlContext.createDataFrame(df7)
df7.show()

def singleExplode(ar):
	rowDict = ar.asDict()
	
	aList = rowDict.pop("synonyms.synonym._VALUE")
	for a in zip(aList):
		newDict = dict(rowDict)
		newDict['Synonyms'] = a
		yield Row(**newDict)


df_split3 = sqlContext.createDataFrame(df7.rdd.flatMap(singleExplode))
df_split3.show()
df_split3.printSchema()
df_split3 = df_split3.toPandas()
df_split3= df_split3.join(pd.DataFrame(df_split3["Synonyms"].tolist(), columns=['DRUG_SYNONYM']))
df_split3 = df_split3.drop(['Synonyms'], axis=1)


df_split3.drop_duplicates(subset=["drugbank-id._VALUE[0]","DRUG_SYNONYM"],keep="first",inplace=True)
df_split3.to_csv(outFileName4,sep='\t', index=False,encoding='utf-8')