#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd


#code to filter human the disease 
with open("CTDn_diseases.tsv",'wb') as wr: 
 
 wr.write(" DiseaseName	DiseaseID	AltDiseaseIDs	Definition	ParentIDs	TreeNumbers	ParentTreeNumbers	Synonyms	SlimMappings\n")
 count =0
 count1=0
 val=0
 om = set()
 lines = []
 u_dis=set()
 u_gene=set()

 with open('CTD_diseases.tsv', 'r') as f:
    for line in f:
     if line.startswith('#'):
        continue
     else:
       line = line[:-1]
       lines=line.split("\t")
       count1=count1+1
       wr.write(line + "\n")
         
       print(u_dis.add(lines[1]))
         
    
       
f.close()
print count1
 
print "======================"      



print u_dis
print(len(u_dis))


