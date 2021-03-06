#CODE2---To filter the file with interventional study type and prepare a file list of file name----
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import xml.etree.ElementTree as ET
import glob, os, shutil


path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/drugintervention/*.xml'
files = glob.glob(path)
count = 0
count1 = 0
count2 = 0
a = set()

with open("/home/16AT72P01/EstimateFile/inventionfilestudy.csv" ,'w') as csv_file:
 	writer = csv.writer(csv_file)
 	writer.writerow(["InventionStudyFileName"])
	
 	for name in files:
 		with open(name) as xml_file1:
 			count = count + 1
 			tree = ET.parse(xml_file1)
 			root = tree.getroot()
 			testValue = root.find('study_type').text
 			print(testValue)
 			count1 = count1 + 1
 			if testValue == "Interventional":
 				a.add(name)
 				writer.writerow([name])
 		print("yes")
 	print(count)
 	print(count1)
 	count2 = len(a)
 	print(count2)
 	csv_file.close()
 	print("=================")


#CODE2a---Remove the set of file to another directory----
dst = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/interventionstudy' #Path you want to move your files to
source = "/home/16AT72P01/EstimateFile/inventionfilestudy.csv"
with open(source) as f1:
	reader = csv.DictReader(f1)
	for row in reader:
		print(row["InventionStudyFileName"])
		if os.path.isfile(row["InventionStudyFileName"]):
			shutil.copy2(row["InventionStudyFileName"], dst)
f1.close()

