#CODE4---To match with DRUGBANK drug list and extract the data from clinical trials----
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import xml.etree.ElementTree as ET
import glob, os, shutil

#List of all drug names present in drugBank dictionary
source = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/DrugBankList.csv"
#List of all synonyms of each drug types
source1 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/drugSynonym.csv"

drugname = set()
with open(source) as f1:
 	reader = csv.DictReader(f1,delimiter='\t')
 	for row in reader:
 		drugname.add(row["name"])

with open(source1) as f2:
 	reader = csv.DictReader(f2,delimiter='\t')
 	for row in reader:
 		drugname.add(row["DRUG_SYNONYM"])

print(drugname)
print(len(drugname))
print("---------------------")


path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/adverseevent/*.xml'
files = glob.glob(path)
count = 0
count1 = 0
count2 = 0
a = set()

with open("/home/16AT72P01/EstimateFile/drugmatchfile.csv" ,'w') as csv_file:
 	writer = csv.writer(csv_file)
 	writer.writerow(["DrugMatchName"])
	
 	for name in files:
 		with open(name) as xml_file1:
 			count = count + 1
 			tree = ET.parse(xml_file1)
 			root = tree.getroot()
 		for intervention in root.findall('intervention'):
 			count1 = count1 + 1
 			testValue = intervention.find('intervention_name').text
 			print(testValue)
 			if testValue in drugname:
 		     		a.add(name)
 		     		writer.writerow([name])
 		     		break
 		print("yes")
 	print(count)
 	print(count1)
 	count2 = len(a)
 	print(count2)
 	csv_file.close()
 	print("=================")



#CODE4a---check duplicate file name----

unique = set()
source = "/home/16AT72P01/EstimateFile/drugmatchfile.csv"
with open(source) as f1:
	reader = csv.DictReader(f1)
	for row in reader:
		unique.add(row["DrugMatchName"])
print("----------")
print(len(unique))



#CODE4b---Remove the set of file to another directory----
dst = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/matchdrug' #Path you want to move your files to
source = "/home/16AT72P01/EstimateFile/drugmatchfile.csv"
with open(source) as f1:
	reader = csv.DictReader(f1)
	for row in reader:
		print(row["DrugMatchName"])
		if os.path.isfile(row["DrugMatchName"]):
			shutil.copy2(row["DrugMatchName"], dst)
f1.close()
