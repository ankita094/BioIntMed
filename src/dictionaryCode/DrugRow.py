#To prepare attribute values for drug data for experimental property done in DrugBank dataset
#Python 3.6.5 |Anaconda, Inc.

import pandas as pd 
import csv


INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/drugAtt1.csv" 
OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/drugAtt2.csv" 

allvalue= []

df = pd.read_csv(INPUT_PATH, sep='\t')


with open("/home/16AT72P01/Excelra/Drugbank/drugAtt2.csv" ,'w') as csv_file:
	writer = csv.writer(csv_file, delimiter ="\t")
	writer.writerow(["drugbank_id","drug_name","description","state","groups","indication","pharmacodynamics","mechanism",\
	"toxicity","metabolism","half_life","direct_parent","kingdom","superclass","class","subclass","atc_code","melting_point","hydrophobicity",\
	"isoelectric","molecular_weight","molecular_formula"])
	for index,row in df.iterrows():
	    
		mergevalue = dict(zip(df['experimental-properties.property.kind'],df['experimental-properties.property.value']))
		print(mergevalue['Isoelectric Point'].values)
		writer.writerow(a)
		allvalue = [str(row['drugbank-id._VALUE[0]']),str(row['name']),str(row['description']),str(row['state']),str(row['groups.group']),str(row['indication']),str(row['pharmacodynamics']),\
		str(row['mechanism-of-action']),str(row['toxicity']),str(row['metabolism']),str(row['half-life']),str(row['classification.direct-parent']),str(row['classification.kingdom']),\
		str(row['classification.superclass']),str(row['classification.class']),str(row['classification.subclass']),str(row['atc-codes.atc-code._code'][0]),\
		str(row['experimental-properties.property.value'].split("',")[0].split()[0][2:]),str(row['experimental-properties.property.value'].split("',")[1][2:-1]),\
		str(row['experimental-properties.property.value'].split("',")[2][2:-1]),str(row['experimental-properties.property.value'].split("',")[3][2:-1]),\
		str(row['experimental-properties.property.value'].split("',")[4][2:-2])]
		
		writer.writerow(a)
		allvalue = []