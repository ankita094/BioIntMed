#To extract for drug data for the main drug table
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




INPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGCHEMICAL.tsv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGCHEMICAL1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')


INPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGDOSAGES.csv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGDOSAGES1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')



INPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGSYNONYMS.csv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGSYNONYMS1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')


INPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGTARGET.tsv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/DRUGTARGET1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')


INPUT_PATH = "/home/16AT72P01/Excelra/sample/TARGETTABLE.tsv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/TARGETTABLE1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')


INPUT_PATH = "/home/16AT72P01/Excelra/sample/EXPERIMENTALPROPERTY.csv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/sample/EXPERIMENTALPROPERTY1.csv" 
df = sqlContext.read.format("csv").option("header", "true").option("sep","\t").load(INPUT_PATH)
#df.show()
#df1 = df.na.fill("NO_DATA")
#df1.show()
df1 = df.toPandas().fillna("NO_DATA")
df1.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')

