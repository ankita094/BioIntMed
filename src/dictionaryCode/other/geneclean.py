#To extract for gene from Homo_sapiens.gene_info data
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv
import os

dst = '/home/16AT72P01/Excelra/Gene/output/gene_table.csv' 
source = "/home/16AT72P01/Excelra/Gene/Homo_sapiens.gene_info"
uniquegene = set()
count = 0
with open(dst,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["symbol","full_name","gene_type","organism","synonyms","chromosome","locus","source"])
	with open(source) as f1:
		reader = csv.DictReader(f1 ,delimiter='\t')
		for row in reader:
			count = count + 1
			uniquegene.add(row["Symbol"])
			writer.writerow([row["Symbol"],row["description"],row["type_of_gene"],"Homo sapiens",row["Synonyms"],\
				row["chromosome"],row["map_location"],row["dbXrefs"]])
	f1.close()
csv_file.close()

print(count)
print(len(uniquegene))

