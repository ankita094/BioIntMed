#Code4---Consider only those row having drugbank ID The connection between drug and metabolites
#Python 3.6.5 |Anaconda, Inc.

import sys
import glob
import errno
import csv

path = '/home/16AT72P01/Excelra/SMPDB/output/metabolics.csv'
files = glob.glob(path)
unique_path = set()

with open("/home/16AT72P01/Excelra/SMPDB/output/metabolic_drug1.csv" ,'w',encoding='utf8') as csv_file:
	writer = csv.writer(csv_file, delimiter='\t')
	writer.writerow(["SMPDB_ID","PATHWAY_NAME","PATHWAY_LABEL","METABOLIC_ID","METABOLIC_NAME","DRUGBANK_ID","KEGG_ID"])
	
	for name in files: 
		try:
			with open(name) as f1:

			    #reader = csv.reader(f1)
			    print(name)
			    reader = csv.DictReader(f1, quotechar='"', delimiter='\t', quoting=csv.QUOTE_ALL, skipinitialspace=True)
			    print(reader)
			    for row in reader:
			    	print(row)
			    	if row["DRUGBANK_ID"] != '':
			    		writer.writerow([row["SMPDB_ID"],row["PATHWAY_NAME"],row["PATHWAY_LABEL"],row["METABOLIC_ID"],row["METABOLIC_NAME"],row["DRUGBANK_ID"],row["KEGG_ID"]])
			    		unique_path.add(row["PATHWAY_NAME"])
			    	else:
			    		print("-------------------")
			    f1.close()
		except IOError as exc:
			if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
				raise # Propagate other kinds of IOError.
	csv_file.close()
print(len(unique_path))