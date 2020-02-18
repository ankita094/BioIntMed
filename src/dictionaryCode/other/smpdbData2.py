#CODE2---First concatenating the required files into one based on the specfic attribute columns from SMPDB database---
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/SMPDB/smpdb_pathways/smpdb_pathways.csv'

with open("/home/16AT72P01/Excelra/SMPDB/output/pathways.csv" ,'w') as csv_file:
	writer = csv.writer(csv_file,quotechar='"', delimiter='\t', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	writer.writerow(["SMPDB_ID","PATHWAY_NAME","PATHWAY_LABEL","DESCRIPTION"])
	with open(path) as f1:
			    #reader = csv.reader(f)
			    count = 0
			    reader = csv.DictReader(f1, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
			    for row in reader:
			    	count = count+1
			    	print(count)
			    	#print(row["SMPDB ID"])
			    	writer.writerow([row["SMPDB ID"],row["Name"],row["Subject"],row["Description"]])

			    f1.close()
	
csv_file.close()

