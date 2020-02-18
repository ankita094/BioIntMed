#CODE7---To filter the attribute value from clinical trial for all intervention genetic only----
#Python 3.6.5 |Anaconda, Inc.

import json
import csv
import glob
from collections import Counter, OrderedDict


OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/" 
outFileName1 = OUTPUT_PATH + "geneticDrug.csv"
outFileName2 = OUTPUT_PATH + "countgeneticdrug.csv"

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/clinicaljson/*.json'
files = glob.glob(path)

uniqueDrug = set()
listDrug = []


class OrderedCounter(Counter, OrderedDict):
    pass

def jsonRead(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":

	with open(outFileName1,"w",encoding='utf8') as csv_file:
		writer = csv.writer(csv_file,delimiter='\t')
		writer.writerow(["clinical_id","geneticdrug_name"])
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
			    		if data['clinical_study']['intervention']:
				    		for loc in data['clinical_study']['intervention']:
				    			if loc["intervention_type"] == "Genetic":
					    			val2 = loc['intervention_name']
					    			print(val2)
					    			uniqueDrug.add(val2)
					    			listDrug.append(val2)
					    			writer.writerow([val1,val2])
					    			print("------------")
			    	except:
			    		continue
	print(len(uniqueDrug))
	csv_file.close()

eventListCount = OrderedCounter(listDrug)

print("There are {} unique words".format(len(listDrug)))
print('They are')


with open(outFileName2,"w",encoding='utf8') as csv_file1:
		writer1 = csv.writer(csv_file1,delimiter='\t')
		writer1.writerow(["geneticdrug_browse","frequency"])
		for k, v in eventListCount.items():
			writer1.writerow([k,v])
csv_file1.close()

