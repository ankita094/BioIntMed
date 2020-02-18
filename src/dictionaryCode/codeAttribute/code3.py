#CODE3---To extract for drug data for the main drug table----
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



#----------CODE3--------
#Part executing for atc code
outFileName2 = OUTPUT_PATH + "atcCode1.csv"

df2 = df.select(df['drugbank-id']['_VALUE'][0],df['name'],df['atc-codes']['atc-code']['_code'],df['atc-codes']['atc-code']['level'])
df2.show()
df5 = df2.toPandas().dropna(thresh=1,subset=('atc-codes.atc-code._code','atc-codes.atc-code.level'))
df5 = sqlContext.createDataFrame(df5)
#df2.toPandas().to_csv(outFileName1,sep='\t', index=False,encoding='utf-8')



#------trial1 to seperate row-------------------------
def dualExplode(a):
    rowDict = a.asDict()
    # print(rowDict)
    bList = rowDict.pop('atc-codes.atc-code._code')
    cList = rowDict.pop('atc-codes.atc-code.level')
    # print(bList)
    # print(len(cList))
    finalList = zip(bList, cList)
    # print(finalList)
    
    for b,c in zip(bList, cList):
        newDict = dict(rowDict)
        newDict['atc-codes.atc-code._code'] = b
        newDict['atc-codes.atc-code.level'] = c
        yield Row(**newDict)

df_split = sqlContext.createDataFrame(df5.rdd.flatMap(dualExplode))

df_split.show()
df_split = df_split.toPandas()
df_split1= df_split.join(pd.DataFrame(df_split["atc-codes.atc-code.level"].tolist(), columns=['R1', 'R2','R3','R4']))

print(df_split1)

df_split1['LEVEL4'] = df_split1.R1.str[0] 
df_split1['CODE4'] = df_split1.R1.str[1]    
df_split1['LEVEL3'] = df_split1.R2.str[0]    
df_split1['CODE3'] = df_split1.R2.str[1]    
df_split1['LEVEL2'] = df_split1.R3.str[0]    
df_split1['CODE2'] = df_split1.R3.str[1]    
df_split1['LEVEL1'] = df_split1.R4.str[0]    
df_split1['CODE1'] = df_split1.R4.str[1]    

df_split1 = df_split1.drop(['atc-codes.atc-code.level','R1', 'R2','R3','R4'], axis=1)
df_split1.to_csv(outFileName2,sep='\t', index=False,encoding='utf-8')
