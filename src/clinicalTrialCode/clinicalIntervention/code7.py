#CODE7---To filter the attribute value from clinical trial for all intervention or drug----


import json
import csv
import glob
from collections import Counter, OrderedDict


OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/" 
outFileName1 = OUTPUT_PATH + "drug1.csv"
outFileName2 = OUTPUT_PATH + "countdrug1.csv"

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/clinicaljson/*.json'
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
		writer.writerow(["clinical_id","drug_name"])
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

			    		if data['clinical_study']['intervention_browse']:
			    			for loc in data['clinical_study']['intervention_browse']["mesh_term"]:
			    				if len(loc)!= 1:
		    						val2 = loc
		    						print(val2)
		    						uniqueDrug.add(val2)
				    				listDrug.append(val2)
				    				writer.writerow([val1,val2])
				    			
		    					else:
		    						val2 = data['clinical_study']['intervention_browse']["mesh_term"]
		    						print(val2)
		    						print("==================")
				    				uniqueDrug.add(val2)
				    				listDrug.append(val2)
				    				writer.writerow([val1,val2])
				    				break
				    			
			    	except:
			    		continue

print("Unique Drug types")
print(len(uniqueDrug))
csv_file.close()



eventListCount = OrderedCounter(listDrug)

print("There are {} unique words".format(len(listDrug)))
print('They are')

with open(outFileName2,"w",encoding='utf8') as csv_file1:
		writer1 = csv.writer(csv_file1,delimiter='\t')
		writer1.writerow(["drug_browse","frequency"])
		for k, v in eventListCount.items():
			writer1.writerow([k,v])
csv_file1.close()
