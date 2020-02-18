#Python 3.6.5 |Anaconda, Inc.

import csv
import pandas as pd


#code to filter human the chem-gene interaction
with open("CTD_chemgene_interaction.tsv",'wb') as wr: 
 
 wr.write("ChemicalName,ChemicalID,CasRN,GeneSymbol,GeneID,GeneForms,Organism,OrganismID,Interaction,InteractionActions,PubMedIDs\n")
 count =0
 count1=0
 lines = []
 u_gene=set()
 uu_gene=set()
 u_chem=set()
 with open("CTD_uniquegene.tsv",'wb') as w: 
  w.write("GeneSymbol,GeneID,GeneForms")
  with open('CTD_chem_gene_ixns.tsv', 'r') as f:
    for line in f:
     if line.startswith('#'):
        continue
     else:
       count=count+1
       line = line[:-1]
       lines=line.split("\t")
       if lines[6]=="Homo sapiens":
         count1=count1+1
         wr.write(line + "\n")
         print(u_gene.add(lines[1]))
         print(uu_gene.add(lines[1]))
         print(u_chem.add(lines[4]))
f.close()
