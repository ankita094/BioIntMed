#CODE2---For preparing the list of side-effect from SIDER database---
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/OFFSIDES/output/adverse_effect2.tsv'
files = glob.glob(path)

unique_sideeffect1 = set()
unique_drug1 = set()
unique_pair1 = set()

with open(path) as f1:
	reader = csv.DictReader(f1, quotechar='"', delimiter='\t', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	print(reader)
	for row in reader:
		unique_drug1.add(row['drug_name'])
		unique_sideeffect1.add(row['adverse_effect'])
		val1 = row['drug_name']+"|"+row['adverse_effect']
		unique_pair1.add(val1)
f1.close()
print(len(unique_drug1))
print(len(unique_sideeffect1))
print(len(unique_pair1))

print(len(unique_drug.intersection(unique_drug1)))
print(len(unique_sideeffect.intersection(unique_sideeffect1)))
print(len(unique_pair.intersection(unique_pair1)))

print(unique_pair.intersection(unique_pair1))


#The file where combine result of both SIDER and OFFSIDES is stored
OUTPUT = "/home/16AT72P01/Excelra/SIDER1/output/SIDEEFFECT1.csv"
count= 0
with open(OUTPUT,"w",encoding='utf8') as f2:
	writer = csv.writer(f2,quotechar='"', delimiter='\t', )
	writer.writerow(["drug_name","adverse_effect"])
	for val in unique_pair:
		if val not in unique_pair.intersection(unique_pair1):
			count = count+1
			key = val.split("|")
			print(key[0])
			writer.writerow([key[0],key[1]])
		else:
			continue

	for val in unique_pair1:
		if val not in unique_pair.intersection(unique_pair1):
			count = count+1
			key = val.split("|")
			print(key[0])
			writer.writerow([key[0],key[1]])
		else:
			continue

	for val in unique_pair.intersection(unique_pair1):
		count = count+1
		key = val.split("|")
		print(key[0])
		writer.writerow([key[0],key[1]])

f2.close()
print(count)
		

	