#CODE1---For checking unique no. of targets---
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/Drugbank/TARGETTABLE1.tsv'
files = glob.glob(path)

unique_target = set()

with open(path) as f1:
	reader = csv.DictReader(f1, quotechar='"', delimiter='\t')
	print(reader)
	for row in reader:
		unique_target.add(row['TARGET_NAME'])
		
f1.close()
print(len(unique_target))
