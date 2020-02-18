#CODE2---Remove the set of file to another directory----
#Python 3.6.5 |Anaconda, Inc.

import glob, os, shutil
import csv

destination = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/geneticintervention' #Path you want to move your files to
source = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/geneticinventionfile.csv"
with open(source) as f1:
	reader = csv.DictReader(f1)
	for row in reader:
		print(row["InventionGeneticFileName"])
		if os.path.isfile(row["InventionGeneticFileName"]):
			shutil.copy2(row["InventionGeneticFileName"], destination)
f1.close()
