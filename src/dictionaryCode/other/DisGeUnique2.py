#CODE2---For calculating pathway details----
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

#path = '/home/16AT72P01/Excelra/SMPDB/output/metabolic_proteins.csv'
path = '/home/16AT72P01/Excelra/SMPDB/output/metabolics.csv'

files = glob.glob(path1)

unique_pathway = set()

with open(path) as f1:
	reader = csv.DictReader(f1, quotechar='"', delimiter='\t')
	print(reader)
	for row in reader:
		#unique_pathway.add(row['PATHWAY_NAME'])
		unique_pathway.add(row['PATHWAY_NAME'])
		
f1.close()
print(len(unique_pathway))
