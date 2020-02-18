#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd


#code to filter human the unique gene information
c=0 

with open("CTD_uniquegene.tsv",'wb') as w: 
  w.write("GeneSymbol\tGeneID\tGeneForms\n")
  with open('CTD_chem_gene_ixns.tsv', 'r') as f:
   for val in uu_gene:
    a=val
    for line in f:
     if line.startswith('#'):
        continue
     else:
       if val in line:
        line = line[:-1]
        lines=line.split("\t")
        if lines[6]=="Homo sapiens":
         w.write(lines[3]+"\t"+lines[4]+"\t"+lines[5]+"\n")
         print val
         c=c+1
       
         uu_gene.remove(a)
  
  