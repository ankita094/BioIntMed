#To extract for drug action on which part physiological system by extracting the information about ATC code and considering only the first label
#Spark version 2.3.1

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *

from pyspark.sql.functions import UserDefinedFunction
import pyspark.sql.functions as fun
from pyspark.sql.functions import Column,udf,lit,collect_list,collect_set
import pandas as pd
from pyspark.sql.types import StringType
from pyspark.sql.functions import explode,split


config = SparkConf().setAll([('spark.master','local[4]'),('spark.executor.memory', '10g'), ('spark.executor.cores', '6'), ('spark.cores.max', '6'), ('spark.driver.memory','10g'),("spark.driver.maxResultSize",'3g')])
scc = SparkContext(conf=config)
sqlContext = SQLContext(scc)


#Code for getting the relation table for physiological systems
concat_list = udf(lambda lst:"|".join(lst),StringType()) 

INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/atcCode1.csv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/Relation/drugPhysioRel1.csv" 

df = sqlContext.read.format("csv").option("header","true").option("delimiter","\t").load(INPUT_PATH)
df.show(10,False)

grouped_df = df.groupby("`drugbank-id._VALUE[0]`","name").agg(concat_list(collect_set("`LEVEL1`")))

grouped_df.show(10,False)

grouped_df = grouped_df.withColumn('PHYSIOLOGICALSYSTEM',explode(split('`<lambda>(collect_set(LEVEL1, 0, 0))`','\\|')))
grouped_df.printSchema()
grouped_df = grouped_df.drop("<lambda>(collect_set(LEVEL1, 0, 0))")
grouped_df.show()

grouped_df.toPandas().to_csv(OUTPUT_PATH,sep='\t', index=False,encoding='utf-8')
	