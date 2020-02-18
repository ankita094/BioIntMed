#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd


#code to filter human the Chemicals details 
with open("CTDn_chemicals.tsv",'wb') as wr: 
 
 wr.write("ChemicalName	ChemicalID	CasRN	Definition	ParentIDs	TreeNumbers	ParentTreeNumbers	Synonyms	DrugBankIDs\n")
 count =0
 count1=0
 val=0
 om = set()
 lines = []
 u_dis=set()
 u_gene=set()

 with open('CTD_chemicals.tsv', 'r') as f:
    for line in f:
     if line.startswith('#'):
        continue
     else:
       line = line[:-1]
       lines=line.split("\t")
       count1=count1+1
       wr.write(line + "\n")
         
       print(u_gene.add(lines[1]))
       print(u_dis.add(lines[8]))
         
    
       
f.close()
print count1
 
print "======================"      



#print u_gene
print(len(u_gene))
print(len(u_dis))
