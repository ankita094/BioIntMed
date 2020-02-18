#----CODE3 For preparing the list of side-effect from SIDER database
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/SIDER1/output/adverse_effects.tsv'
files = glob.glob(path)

unique_drug = set()

with open(path) as f1:
	reader = csv.DictReader(f1, delimiter='\t')
	print(reader)
	for row in reader:
		unique_drug.add(row['drug_name'])
		
f1.close()
print(len(unique_drug))


path = '/home/16AT72P01/Excelra/OFFSIDES/output/adverse_effect2.tsv'
files = glob.glob(path)


with open(path) as f1:
	reader = csv.DictReader(f1,delimiter='\t')
	print(reader)
	for row in reader:
		unique_drug.add(row['drug_name'])
f1.close()
print(len(unique_drug))


#the file where combine result of both SIDER and OFFSIDES is stored
OUTPUT ="/home/16AT72P01/Excelra/SIDER1/output/DRUGMAP.csv"
INPUT = "/home/16AT72P01/Excelra/Drugbank/mainDrug1.csv"
count= 0
with open(OUTPUT,"w",encoding='utf8') as f2:
	writer = csv.writer(f2,quotechar='"', delimiter='\t')
	writer.writerow(["drugbank_id","drug_name"])
	for val in unique_drug:
		with open(INPUT,"r") as csv_file:
			reader = csv.DictReader(csv_file, delimiter='\t')
			for row in reader:
				print(row["name"])
				if val.lower() == row["name"].lower():
					count=count+1
					print("-----------------------")
					writer.writerow([row["drugbank-id._VALUE[0]"],val])
					break
				else:
					continue
		csv_file.close()

f2.close()
print(count)
		



	