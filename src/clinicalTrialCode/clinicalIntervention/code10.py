#CODE10---checking with the FDA approved drug from drugBank list and creating new file with FDA level----
#Python 3.6.5 |Anaconda, Inc.

import csv

inputFileName1 = "/home/16AT72P01/EstimateFile/mainDrug1.csv"
inputFileName2 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/countdrug1.csv"
inputFileName3 = "/home/16AT72P01/EstimateFile/drugSynonym.csv"

synlist = set()
list1 = set()
list2 = set()
with open(inputFileName1,"r",encoding='utf8') as csv_file1:
 	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
 	  			for row in reader:
 	  				if( (row["groups.group"] == "['approved']") or (row["groups.group"] == "['approved', 'experimental']") or (row["groups.group"] == "['approved', 'experimental', 'investigational']") or (row["groups.group"] == "['approved', 'investigational']")):
 	  					print(row["groups.group"])
 	  					list1.add(row['name'])
 	  					synlist.add(row['drugbank-id._VALUE[0]'])
 	  				else:
 	  					continue
csv_file1.close()

#---To check the synonym of each FDA drugs also-----------
with open(inputFileName3,"r",encoding='utf8') as csv_file1:
 	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
 	  			for row in reader:
 	  				if( row["drugbank-id._VALUE[0]"] in synlist):
 	  					list1.add(row['DRUG_SYNONYM'])
 	  				else:
 	  					continue
csv_file1.close()

with open(inputFileName2,"r",encoding='utf8') as csv_file1:
 	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
 	  			for row in reader:
 	  				list2.add(row['drug_browse'])
csv_file1.close()

list3 = list1.intersection(list2)
print(list3)
print("No.of FDA approved drugs")
print(len(list1))
print(len(list2))
print(len(list3))

# use the list of FDA approve drug and create another file from it
inputFileName4 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/drug1.csv"
outputFileName1 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/fdaDrugFile.csv"
count = 0
uniqueFDA = set()
with open(outputFileName1,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["clinical_id","drug_name","FDA_approval_flag"])
	with open(inputFileName4,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				if row["drug_name"] in list3:
	  					count = count + 1
	  					uniqueFDA.add(row["drug_name"])
	  					writer.writerow([row["clinical_id"],row["drug_name"],"yes"])
	  				else:
	  					writer.writerow([row["clinical_id"],row["drug_name"],"No"])

	csv_file1.close()
csv_file.close()
print("No of FDA drug count")
print(count)
print(len(uniqueFDA))
