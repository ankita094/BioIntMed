#To count all unique relational property type in detail.
#Python 3.6.5 |Anaconda, Inc.

import sys
import csv
csv.field_size_limit(sys.maxsize)
from collections import Counter


#To get the count of each type sevierity of entity
with open("/home/16AT72P01/Excelra/Drugbank/Relation/uniqueInteractionCount.csv","w") as csvfile2:
	with open("/home/16AT72P01/Excelra/Drugbank/Relation/drugInteractionRel2.csv","r") as csvfile1:
		reader = csv.DictReader(csvfile1, delimiter='\t')
		list1 = []
		list2 = set()
		for row in reader:
			list1.append(row['FunctionalComponent'])
			list2.add(row['FunctionalComponent'])
		print(len(list1))
		print(len(list2))
		counter = Counter(list1)
	#print(counter)
	for key,value in counter.items():
			#print(key)
			#print(value)
			print("------------")
			csvfile2.write(str(key)+"\t"+str(value)+"\n")
csvfile2.close()
csvfile1.close()

#To get the count of each type target action of entity
with open("/home/16AT72P01/Excelra/Drugbank/Relation/uniqueTargetCount.csv","w") as csvfile2:
	with open("/home/16AT72P01/Excelra/Drugbank/Relation/drugTargetRelation2.tsv","r") as csvfile1:
		reader = csv.DictReader(csvfile1, delimiter='\t')
		list1 = []
		list2 = set()
		for row in reader:
			list1.append(row['ACTION'])
			list2.add(row['ACTION'])
		print(len(list1))
		print(len(list2))
		counter = Counter(list1)
	#print(counter)
	for key,value in counter.items():
			#print(key)
			#print(value)
			print("------------")
			csvfile2.write(str(key)+"\t"+str(value)+"\n")

csvfile2.close()
csvfile1.close()

#To get the count of each physiology based on first alphabet of ATC code of entity
with open("/home/16AT72P01/Excelra/Drugbank/Relation/uniquePhysiologyCount.csv","w") as csvfile2:
	with open("/home/16AT72P01/Excelra/Drugbank/Relation/drugPhysioRel1.csv","r") as csvfile1:
		reader = csv.DictReader(csvfile1, delimiter='\t')
		list1 = []
		list2 = set()
		for row in reader:
			list1.append(row['PHYSIOLOGICALSYSTEM'])
			list2.add(row['PHYSIOLOGICALSYSTEM'])
		print(len(list1))
		print(len(list2))
		counter = Counter(list1)
	#print(counter)
	for key,value in counter.items():
			#print(key)
			#print(value)
			print("------------")
			csvfile2.write(str(key)+"\t"+str(value)+"\n")

csvfile2.close()
csvfile1.close()
			
		