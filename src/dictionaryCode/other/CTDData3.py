#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd


#code to filter human the chem-disease interaction
with open("CTD_curated_chemicals_diseases.tsv",'wb') as wr: 
 
 wr.write("ChemicalName	ChemicalID	CasRN	DiseaseName	DiseaseID	DirectEvidence	InferenceGeneSymbol	InferenceScore	OmimIDs	PubMedIDs\n")
 count =0
 count1=0
 val=0
 om = set()
 lines = []
 u_dis=set()
 u_chem=set()

 with open('CTD_chemicals_diseases.tsv', 'r') as f:
    for line in f:
     if line.startswith('#'):
        continue
     else:
       count=count+1
       line = line[:-1]
       lines=line.split("\t")
       if lines[5]=="therapeutic" or lines[5]=="marker" or lines[5]=="mechanism" or lines[5]=="marker/mechanism" or lines[5]=="marker/mechanism or therapeutic":
         count1=count1+1
         wr.write(line + "\n")
         print(om.add(lines[8]))
       print(u_dis.add(lines[4]))
         
       print(u_chem.add(lines[1]))
       
f.close()

print "======================"      
print count
print count1

print u_dis
print(len(u_dis))
print(len(u_chem))
print (len(om))
