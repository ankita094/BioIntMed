#CODE5---To give estimation of all drug,disese,group,approved drug etc from drugBank source----
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import xml.etree.ElementTree as ET

#List of all FDA approve drug and its synonyms
source = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/approveDrug.csv"
source1 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/drugSynonym.csv"

approveddrugname = set()
idlist = set()
with open(source) as f1:
 	reader = csv.DictReader(f1,delimiter='\t')
 	for row in reader:
 		if "approved" in row["groups.group"]:
 			idlist.add(row["drugbank-id._VALUE[0]"])
 			approveddrugname.add(row["name"])
 		else:
 			print(row["groups.group"])

with open(source1) as f2:
	reader = csv.DictReader(f2,delimiter='\t')
	for row in reader:
		if row["drugbank-id._VALUE[0]"] in idlist:
			approveddrugname.add(row["DRUG_SYNONYM"])

print(approveddrugname)
print(len(approveddrugname))
print("---------------------")

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/matchdrug/*.xml'
files = glob.glob(path)
count = 0
count1 = 0
count2 = 0
allDrug = set()
approvedDrug = set()
diseaseValue = set()
adverseEvent = set()
adverseCategory = set()

for name in files:
	with open(name) as xml_file1:
		count = count + 1
		tree = ET.parse(xml_file1)
		root = tree.getroot()
	for intervention in root.findall('intervention'):
		testValue = intervention.find('intervention_name').text
		print(testValue)
		allDrug.add(testValue)
		if testValue in approveddrugname:
			approvedDrug.add(testValue)

	for disease in root.findall("condition_browse"):
		for mesh in disease.findall('mesh_term'):
			diseaseValue.add(mesh.text)
			print(mesh.text)

	for reported in root.findall("./clinical_results/reported_events/other_events/category_list/category/event_list/"):
			if reported.find("sub_title") is not None:
				testValue1 = reported.find("sub_title").text
				adverseEvent.add(testValue1)
				print(testValue1)


	for reported1 in root.findall("./clinical_results/reported_events/other_events/category_list/category/"):
				if reported1.find("title") is not None:
					testValue1 = reported1.find("title").text
					adverseCategory.add(testValue1)
					print(testValue1)


print(diseaseValue)
print(count)
print(len(allDrug))
print(len(approvedDrug))
print(len(diseaseValue))
print(len(adverseEvent))
print(len(adverseCategory))
print("=================")