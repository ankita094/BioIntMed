#CODE8 ----To calculate the trial frequency for drug entity----
##Python 3.6.5 |Anaconda, Inc.


import json
import csv
import glob
from collections import Counter, OrderedDict


INPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/" 
#For drug clinical trail calculation
inputFileName1 = INPUT_PATH + "drug1.csv"
inputFileName2 = INPUT_PATH + "countdrug1.csv"
#For adverse event clinical trail calculation
inputFileName3 = INPUT_PATH + "allAdverseEvent1.csv"
inputFileName4 = INPUT_PATH + "countAllEvent1.csv"
#For disease no.of clinical trial calculation
inputFileName5 = INPUT_PATH + "condition1.csv"
inputFileName6 = INPUT_PATH + "countCondition1.csv"
For adverse category no.of clinical trial calculation
inputFileName7 = INPUT_PATH + "trialCategory1.csv"
inputFileName8 = INPUT_PATH + "countCategory1.csv"

#For drug clinical trail calculation
outputFileName1 = INPUT_PATH + "drugTrialCount.csv"
#For adverse event clinical trail calculation
outputFileName2 = INPUT_PATH + "adverseEventTrialCount.csv"
#For disease no.of clinical trial calculation
outputFileName3 = INPUT_PATH + "conditionTrialCount.csv"
outputFileName4 = INPUT_PATH + "categoryTrialCount.csv"



#---------For drug-clinical trial estimation---------------------
with open(outputFileName1,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["drug_name","countTrials"])
	with open(inputFileName2,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				trialCount1 = set()
	  				drug_name = row['drug_browse']
	  				with open(inputFileName1,"r",encoding='utf8') as csv_file2:
	  					reader1 = csv.DictReader(csv_file2,delimiter ="\t")
	  					for row1 in reader1:
	  						if row1["drug_name"] == drug_name :
	  							print(drug_name)
	  							trialCount1.add(row1['clinical_id'])
	  				csv_file2.close()
	  				writer.writerow([drug_name,len(trialCount1)])
	csv_file1.close()
csv_file.close()


#----------------------For adverseEvent -clinical trial estimation-----------------
with open(outputFileName2,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["adverse_event","countTrials"])
	with open(inputFileName4,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				trialCount1 = set()
	  				adverse_event1 = row['adverse_event']
	  				with open(inputFileName3,"r",encoding='utf8') as csv_file2:
	  					reader1 = csv.DictReader(csv_file2,delimiter ="\t")
	  					for row1 in reader1:
	  						if row1["adverse_event"] == adverse_event1 :
	  							print(adverse_event1)
	  							trialCount1.add(row1['clinical_id'])
	  				csv_file2.close()
	  				writer.writerow([adverse_event1,len(trialCount1)])
	csv_file1.close()
csv_file.close()




#----------------------For condition -clinical trial estimation-----------------
with open(outputFileName3,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["condition","countTrials"])
	with open(inputFileName6,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				trialCount1 = set()
	  				condition = row['condition_browse']
	  				with open(inputFileName5,"r",encoding='utf8') as csv_file2:
	  					reader1 = csv.DictReader(csv_file2,delimiter ="\t")
	  					for row1 in reader1:
	  						if row1["condition"] == condition :
	  							print(condition)
	  							trialCount1.add(row1['clinical_id'])
	  				csv_file2.close()
	  				writer.writerow([condition,len(trialCount1)])
	csv_file1.close()
csv_file.close()

print("All execution done")




#----------------------For adverseCategory-clinical trial estimation------------------
with open(outputFileName4,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["adverse_category","countTrials"])
	with open(inputFileName8,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				trialCount1 = set()
	  				adverse_event1 = row['adverse_category']
	  				with open(inputFileName7,"r",encoding='utf8') as csv_file2:
	  					reader1 = csv.DictReader(csv_file2,delimiter ="\t")
	  					for row1 in reader1:
	  						if row1["adverse_events"] == adverse_event1 :
	  							print(adverse_event1)
	  							trialCount1.add(row1['clinical_id'])
	  				csv_file2.close()
	  				writer.writerow([adverse_event1,len(trialCount1)])
	csv_file1.close()
csv_file.close()

