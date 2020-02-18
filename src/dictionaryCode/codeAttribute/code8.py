#CODE8---To extract for drug data for the main drug table----
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

#------------CODE8----------------
#Extract the data for experimental property

outFileName5 = OUTPUT_PATH + "experimentalProperty.csv"

df10 = df.select(df['drugbank-id']['_VALUE'][0],df['experimental-properties']['property'])

df10 = df10.selectExpr("`drugbank-id._VALUE[0]` as col1", "`experimental-properties.property` as col2")

df10.printSchema()
df10.show(3,False)

'''
|DB00001|[[Melting Point, Otto, A. & Seckler, R. Eur. J. Biochem. 202:67-73 (1991), 65 °C], [Hydrophobicity,, -0.777], [Isoelectric Point,, 4.04], [Molecular Weight,, 6963.425], [Molecular Formula,, C287H440N80O110S6]]                                           |
|DB00002|[[Melting Point, Vermeer, A.W.P. & Norde, W., Biophys. J. 78:394-404 (2000), 61 °C (FAB fragment), 71 °C (whole mAb)], [Hydrophobicity,, -0.413], [Isoelectric Point,, 8.48], [Molecular Weight,, 145781.6], [Molecular Formula,, C6484H10042N1732O2023S36]]|
|DB00003|[[Melting Point, Chan, H.K. et al., Pharm Res. 13:756-761 (1996), 67 °C], [Hydrophobicity,, -0.083], [Isoelectric Point,, 4.58], [Molecular Weight,, 29253.9], [Molecular Formula,, C1321H1999N339O396S9]] 

+---------------------------------------+
|ID|COMP                         |
+---------------------------------------+
|aA|{'API': '201', 'BNQ': '2'}            |
|bB| {'API': '501', 'BNQ': '1', 'IN': '5'}|
+---------------------------------------+

root
 |-- ID: string (nullable = true)
 |-- COMP: string (nullable = true)

'''


def parse1(s):
    dict_v= defaultdict(str)
    try:
        for each in s:
            #print(each)
            dict_v[each[0]] = each[2] 
           #print("-----------------------")
        #print(dict(dict_v))
        return str(dict(dict_v))
    except Exception as e:
        print(e)
        pass

def parse2(s):
	try:
		#print(s)
		#print("----------------------------------")
		return json.loads(s.replace("'", '"'))
	except json.JSONDecodeError:
		pass

parse_udf1 = udf(parse1, StringType()) 
parse_udf2 = udf(parse2, MapType(StringType(), StringType()))
df10 = df10.withColumn('col3', parse_udf1('col2'))
df10 = df10.drop("col2")
df10.count()
#As the dict value contains null value replacing those row
df10 = df10.filter(~reduce(lambda x, y: x & y, [df10['col3'].isNull() for c in df10.columns]))
#df.count()

#df = df.select("col1",  explode(parse_udf2("col3")))

df10 = df10.select("*", explode(parse_udf2("`col3`")))\
    .groupBy("`col1`","`col3`").pivot("key").agg(first("value"))

df10 = df10.drop("col3")

df10.show(10,False)
df10.toPandas().to_csv(outFileName5,sep='\t', index=False,encoding='utf-8')

