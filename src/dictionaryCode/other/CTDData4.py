#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd

#code to filter human the gene-disease interaction
with open("CTD_curated_genes_diseases.tsv",'wb') as wr: 
 
 wr.write("GeneSymbol GeneID  DiseaseName DiseaseID DirectEvidence  InferenceChemicalName InferenceScore  OmimIDs PubMedIDs\n")
 count =0
 count1=0
 val=0
 om = set()
 lines = []
 u_dis=set()
 u_gene=set()

#code to filter the gene-disease interaction
 with open('CTD_genes_diseases.tsv', 'r') as f:
    for line in f:
     if line.startswith('#'):
        continue
     else:
       count=count+1
       line = line[:-1]
       lines=line.split("\t")
       if lines[4]=="therapeutic" or lines[4]=="marker" or lines[5]=="mechanism" or lines[4]=="marker/mechanism" or lines[4]=="marker/mechanism or therapeutic":
         count1=count1+1
         wr.write(line + "\n")
         print(om.add(lines[7]))
       print(u_dis.add(lines[3]))
         
       print(u_gene.add(lines[1]))
       
f.close()

 
print "======================"      
print count
print count1

print u_dis
print(len(u_dis))
print(len(u_gene))
print (len(om))


