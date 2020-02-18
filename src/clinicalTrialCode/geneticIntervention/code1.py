#CODE1---To filter the file with invention type:Genetic and prepare a file list of file name----
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import xml.etree.ElementTree as ET
import glob

path = 'sampleData/clinicalExample/*.xml'
files = glob.glob(path)
count = 0
count1 = 0
count2 = 0
a = set()

with open("/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/geneticinventionfile.csv" ,'w') as csv_file:
 	writer = csv.writer(csv_file)
 	writer.writerow(["InventionGeneticFileName"])
	
 	for name in files:
 		with open(name) as xml_file1:
 			count = count + 1
 			tree = ET.parse(xml_file1)
 			root = tree.getroot()
 		for intervention in root.findall('intervention'):
 			count1 = count1 + 1
 			testValue = intervention.find('intervention_type').text
 			print(testValue)
 			if testValue == "Genetic":
 				a.add(name)
 				writer.writerow([name])
 				break
 		print("yes")
 	print(count)
 	print(count1)
 	count2 = len(a)
 	print(count2)