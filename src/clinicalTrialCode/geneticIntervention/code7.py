#CODE6---To filter the attribute value from clinical trial for genetic invention----
#Python 3.6.5 |Anaconda, Inc.


import json
import csv
import glob
from collections import OrderedDict

OUTPUT_PATH = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/" 
outFileName1 = OUTPUT_PATH + "mainClinical2.csv"
path = '/home/16AT72P01/EstimateFile/CLINICALOUTPUT2/clinicaljson/*.json'
files = glob.glob(path)
count=0

def jsonRead(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":

	with open(outFileName1,"w",encoding='utf8') as csv_file:
		writer = csv.writer(csv_file,delimiter='\t')
		writer.writerow(["clinical_id","title","brief_description","description","phase","study_type","gender","min_age","max_age","intervention_model","primary_purpose","masking","condition","intervention","genetic_intervention","receive_date","result_first","last_updated","last_verified","start_date","completion_date","sponsor"])
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
			    		if data['clinical_study']['official_title']:
			    			value = data['clinical_study']['official_title']
			    			val2 ='"'+value+'"'
			    			print(val2)

			    	except:
			    		val2= "N/A"
			    	try:
			    		if data['clinical_study']['brief_summary']['textblock']:
			    			value1 = data['clinical_study']['brief_summary']['textblock']
			    			val3 ='"'+value1+'"'
			    			print(val3)
			    	except:
			    		val3= "N/A"
			    	try:
			    		if data['clinical_study']['detailed_description']['textblock']:
			    			value2 = data['clinical_study']['detailed_description']['textblock']
			    			val4 = '"'+value2+'"'
			    			print(val4)
			    	except:
			    		val4= "N/A"

			    	try:
			    		if data['clinical_study']['phase']:
			    			val5 = data['clinical_study']['phase']
			    			print(val5)
			    	except:
			    		val5= "N/A"

			    	try:
			    		if data['clinical_study']['study_type']:
			    			val6 = data['clinical_study']['study_type']
			    			print(val6)
			    	except:
			    		val6= "N/A"

			    	try:
			    		if data['clinical_study']['eligibility']['gender']:
			    			val7 = data['clinical_study']['eligibility']['gender']
			    			print(val7)
			    	except:
			    		val7= "N/A"

			    	try:
			    		if data['clinical_study']['eligibility']['minimum_age']:
			    			val8 = data['clinical_study']['eligibility']['minimum_age']
			    			print(val8)
			    	except:
			    		val8= "N/A"

			    	try:
			    		if data['clinical_study']['eligibility']['maximum_age']:
			    			val9 = data['clinical_study']['eligibility']['maximum_age']
			    			print(val9)
			    	except:
			    		val9= "N/A"

			    	try:
			    		if data['clinical_study']['study_design_info']['intervention_model']:
			    			val10 = data['clinical_study']['study_design_info']['intervention_model']
			    			print(val10)
			    	except:
			    		val10= "N/A"

			    	try:
			    		if data['clinical_study']['study_design_info']['primary_purpose']:
			    			val11 = data['clinical_study']['study_design_info']['primary_purpose']
			    			print(val11)
			    	except:
			    		val11= "N/A"

			    	try:
			    		if data['clinical_study']['study_design_info']['masking']:
			    			val12 = data['clinical_study']['study_design_info']['masking']
			    			print(val12)
			    	except:
			    		val12= "N/A"

			    	try:
			    		if data['clinical_study']['condition_browse']['mesh_term']:
			    			val13 = data['clinical_study']['condition_browse']['mesh_term']
			    			print(val13)
			    	except:
			    		val13= "N/A"

			    	try:
			    		if data['clinical_study']['intervention_browse']['mesh_term']:
			    			val21 = data['clinical_study']['intervention_browse']['mesh_term']
			    			print(val21)

			    	except:
			    		val21= "N/A"

			    	try:
			    		if data['clinical_study']['intervention']:
				    		val22 = []
				    		for val in data['clinical_study']['intervention']:
				    			if val["intervention_type"] == "Genetic":
					    			val22.append(val['intervention_name'])
					    			print(val21)

			    	except:
			    		val22= "N/A"


			    	try:
			    		if data['clinical_study']['firstreceived_date']:
			    			val14 = data['clinical_study']['firstreceived_date']
			    			print(val14)
			    	except:
			    		val14= "N/A"

			    	try:
			    		if data['clinical_study']['firstreceived_results_date']:
			    			val15 = data['clinical_study']['firstreceived_results_date']
			    			print(val15)
			    	except:
			    		val15= "N/A"

			    	try:
			    		if data['clinical_study']['lastchanged_date']:
			    			val16 = data['clinical_study']['lastchanged_date']
			    			print(val16)
			    	except:
			    		val16= "N/A"

			    	try:
			    		if data['clinical_study']['verification_date']:
			    			val17 = data['clinical_study']['verification_date']
			    			print(val17)
			    	except:
			    		val17= "N/A"

			    	try:
			    		if data['clinical_study']['start_date']:
			    			val18 = data['clinical_study']['start_date']
			    			print(val18)
			    	except:
			    		val18= "N/A"

			    	try:
			    		if data['clinical_study']['completion_date']['#text']:
			    			val19 = data['clinical_study']['completion_date']['#text']
			    			print(val19)
			    	except:
			    		val19= "N/A"

			    	try:
			    		if data['clinical_study']['sponsors']['lead_sponsor']['agency']:
			    			val20 = data['clinical_study']['sponsors']['lead_sponsor']['agency']
			    			print(val20)
			    	except:
			    		val20= "N/A"

			    	writer.writerow([val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val21,val22,val14,val15,val16,val17,val18,val19,val20])
		print("---------------------------------------")
csv_file.close()
	    	