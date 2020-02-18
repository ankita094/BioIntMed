#CODE4---Remove the set of file to another directory----
#Python 3.6.5 |Anaconda, Inc.

import glob, os, shutil
import csv

dst = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/interventionstudy1' #Path you want to move your files to
source = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/inventionfilestudy1.csv"
with open(source) as f1:
	reader = csv.DictReader(f1)
	for row in reader:
		print(row["InventionStudyFileName"])
		if os.path.isfile(row["InventionStudyFileName"]):
			shutil.copy2(row["InventionStudyFileName"], dst)
f1.close()


