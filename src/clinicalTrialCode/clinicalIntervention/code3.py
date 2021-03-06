#CODE3---To filter the attribute value from clinical trial for other adverse Events----
#Python 3.6.5 |Anaconda, Inc.

import json
import csv
import glob
from collections import Counter, OrderedDict


OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/" 
outFileName1 = OUTPUT_PATH + "trialEvent1.csv"
outFileName2 = OUTPUT_PATH + "countEvent1.csv"

path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT/clinicaljson/*.json'
files = glob.glob(path)
uniqueEvent = set()
listEvent = []

class OrderedCounter(Counter, OrderedDict):
    pass

def jsonRead(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":

	with open(outFileName1,"w",encoding='utf8') as csv_file:
		writer = csv.writer(csv_file,delimiter='\t')
		writer.writerow(["clinical_id","adverse_category","adverse_event"])
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
				    				for loc1 in loc["event_list"]["event"]:
				    					val3 = loc1["sub_title"]
				    					print(val3)
				    					uniqueEvent.add(val3)
				    					listEvent.append(val3)
				    					writer.writerow([val1,val2,val3])
			    			
			    	except:
			    		continue

print("Unique Event types")
print(len(uniqueEvent))
csv_file.close()



eventListCount = OrderedCounter(listEvent)

print("There are {} unique words".format(len(eventListCount)))
print('They are')

with open(outFileName2,"w",encoding='utf8') as csv_file1:
		writer1 = csv.writer(csv_file1,delimiter='\t')
		writer1.writerow(["adverse_event","frequency"])
		for k, v in eventListCount.items():
			writer1.writerow([k,v])
csv_file1.close()
