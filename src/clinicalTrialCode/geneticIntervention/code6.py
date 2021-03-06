#CODE6---To filter the file of adverse events and prepare a file list of file name----
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import glob
import xml.etree.ElementTree as ET

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/interventionstudy1/*.xml'
files = glob.glob(path)
count = 0
count1 = 0
count2 = 0
a = set()

with open("/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/adverseevent.csv" ,'w') as csv_file:
 	writer = csv.writer(csv_file)
 	writer.writerow(["AdverseEventFileName"])
	
 	for name in files:
 		with open(name) as xml_file1:
 			count = count + 1
 			tree = ET.parse(xml_file1)
 			root = tree.getroot()
 		for adverse in root.findall('clinical_results'):
 		    for event in adverse.findall('reported_events'):
 		     	testValue = event.find('other_events')
 		     	print(testValue)
 		     	if testValue is not None:
 		     		a.add(name)
 		     		writer.writerow([name])
 		    print("yes")
 	print(count)
 	print(count1)
 	count2 = len(a)
 	print(count2)
 	csv_file.close()
 	print("=================")
