#CODE5---For combination serious adverse Events and other event mentioned in clinical trials----
#Python 3.6.5 |Anaconda, Inc.

import csv
from collections import Counter, OrderedDict


OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/" 
outFileName1 = OUTPUT_PATH + "allAdverseEvent1.csv"
outFileName2 = OUTPUT_PATH + "countAllEvent1.csv"

path1 = OUTPUT_PATH + "trialEvent1.csv"
path2 = OUTPUT_PATH + "trialSeriousEvent1.csv"

uniqueEvent = set()
listEvent = []
uniqueCategory = set()

class OrderedCounter(Counter, OrderedDict):
     pass

with open(outFileName1,"w",encoding='utf8') as csv_file:
 		writer1 = csv.writer(csv_file,delimiter='\t')
 		writer1.writerow(["clinical_id","adverse_category","adverse_event"])

 		with open(path1,"r",encoding='utf8') as csv_file1:
 			reader = csv.DictReader(csv_file1,delimiter ="\t")
 			for row in reader:
 				print(row['adverse_event'])
 				uniqueEvent.add(row['adverse_event'])
 				listEvent.append(str(row['adverse_event']))
 				writer1.writerow([row["clinical_id"],row["adverse_category"],row["adverse_event"]])
 		csv_file1.close()

 		with open(path2,"r",encoding='utf8') as csv_file1:
 			reader = csv.DictReader(csv_file1,delimiter ="\t")
 			for row in reader:
 				print(row['adverse_event'])
 				uniqueEvent.add(row['adverse_event'])
 				listEvent.append(str(row['adverse_event']))
 				writer1.writerow([row["clinical_id"],row["adverse_category"],row["adverse_event"]])
 		csv_file1.close()
csv_file.close()

print(len(uniqueEvent))
eventListCount = OrderedCounter(listEvent)

with open(outFileName2,"w",encoding='utf8') as csv_file2:
		writer2 = csv.writer(csv_file2,delimiter='\t')
		writer2.writerow(["adverse_event","frequency"])
		for k, v in eventListCount.items():
			writer2.writerow([k,v])
csv_file2.close()
