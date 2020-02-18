# To extract drugname and its comparison with SIDER data.
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


config = SparkConf().setAll([('spark.master','local[4]'),('spark.executor.memory', '10g'), ('spark.executor.cores', '6'), ('spark.cores.max', '6'), ('spark.driver.memory','10g'),("spark.driver.maxResultSize",'3g')])
scc = SparkContext(conf=config)
sqlContext = SQLContext(scc)


#INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/fulldatabase.xml" 
INPUT_PATH = 'sampleData/dictionaryExample/DrugbankExampleData.xml'
INPUT_PATH1 = "/home/16AT72P01/Excelra/SIDER/drug_names.tsv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugout1" 


#Index file containing all the drug name excluding synonym

df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='drug').load(INPUT_PATH)
df.printSchema()
df1 = df.select(df['name'])
df1.show()

df2 =  sqlContext.read.format("csv").option("delimiter", "\t").option("header", "false").load(INPUT_PATH1)
df3 =df2.select('_c1')
df3.show()

df4 = df.select(df['name']).intersect(df2.select('_c1'))
df4.show()
df4.toPandas().to_csv(OUTPUT_PATH,sep='\t', index=False)
  

