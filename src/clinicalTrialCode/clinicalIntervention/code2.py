#CODE2---To filter the attribute value from clinical trial for adverse Category and its respective counts----
#Python 3.6.5 |Anaconda, Inc.

import json
import csv
import glob
from collections import Counter, OrderedDict


OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/" 
outFileName1 = OUTPUT_PATH + "trialCategory1.csv"
outFileName2 = OUTPUT_PATH + "countCategory1.csv"

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/clinicaljson/*.json'
files = glob.glob(path)
uniqueCategory = set()
listCategory = []

class OrderedCounter(Counter, OrderedDict):
    pass

def jsonRead(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":

	with open(outFileName1,"w",encoding='utf8') as csv_file:
		writer = csv.writer(csv_file,delimiter='\t')
		writer.writerow(["clinical_id","adverse_events"])
		for name in files:
		    data = jsonRead(name)
		    for key,value in data.items():
			    	try:
			    		if data['clinical_study']['id_info']['nct_id']:
			    			val1 = data['clinical_study']['id_info']['nct_id']
			    			print(val1)
			    	except:
			    		val1 = "N/A"

			    	try:
			    		if data['clinical_study']["clinical_results"]["reported_events"]["other_events"]["category_list"]["category"]:
			    			for loc in data['clinical_study']["clinical_results"]["reported_events"]["other_events"]["category_list"]["category"]:
				    			val2 = loc["title"]
				    			if val2 != "Total":
				    				uniqueCategory.add(val2)
				    				listCategory.append(val2)
				    				writer.writerow([val1,val2])
			    			
			    	except:
			    		continue

		print("---------------------------------------")

print("Unique Category types")
print(len(uniqueCategory))
csv_file.close()



categoryListCount = OrderedCounter(listCategory)

print("There are {} unique words".format(len(categoryListCount)))
print('They are')

with open(outFileName2,"w",encoding='utf8') as csv_file1:
		writer1 = csv.writer(csv_file1,delimiter='\t')
		writer1.writerow(["adverse_category","frequency"])
		for k, v in categoryListCount.items():
			writer1.writerow([k,v])
csv_file1.close()


