#CODE1---First concatenating the required files into one based on the specfic attribute columns from SMPDB database and getting metabolics---
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/SMPDB/smpdb_metabolites/*.csv'
files = glob.glob(path)

with open("/home/16AT72P01/Excelra/SMPDB/output/metabolics.csv" ,'w') as csv_file:
	writer = csv.writer(csv_file, quotechar='"', delimiter='\t', quoting=csv.QUOTE_ALL, skipinitialspace=True)
	writer.writerow(["SMPDB_ID","PATHWAY_NAME","PATHWAY_LABEL","METABOLIC_ID","METABOLIC_NAME","DRUGBANK_ID","KEGG_ID"])
	
	for name in files: 
		try:
			with open(name) as f1:

			    #reader = csv.reader(f1)
			    print(name)
			    reader = csv.DictReader(f1, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
			    print(reader)
			    for row in reader:
			    	print(row)
			    	writer.writerow([row["SMPDB ID"],row["Pathway Name"],row["Pathway Subject"],row["Metabolite ID"],\
			    		row["Metabolite Name"],row["DrugBank ID"],row["KEGG ID"]])
			    	#writer.writerow([row[0],row[1],row[2],row[3],row[4],row[8],row[6]])


			    f1.close()
		except IOError as exc:
			if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
				raise # Propagate other kinds of IOError.
	csv_file.close()


