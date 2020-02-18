#---To read the schema of the clinical trial file for further analysis----
#Spark version 2.3.1
#Run: spark-submit filename.py

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *


config = SparkConf().setAll([('spark.master','local[4]'),('spark.executor.memory', '10g'), ('spark.executor.cores', '6'), ('spark.cores.max', '6'), ('spark.driver.memory','10g'),("spark.driver.maxResultSize",'3g')])
scc = SparkContext(conf=config)
sqlContext = SQLContext(scc)

INPUT_PATH = 'sampleData/clinicalExample/NCT00001213.xml'

df = sqlContext.read.format('com.databricks.spark.xml').options(rowTag='clinical_study').load(INPUT_PATH)
df.printSchema()