#To extract the chemical property and map those to pubChem database to extract multiple features or chemical properties script 2
#Python 3.6.5 |Anaconda, Inc.

import os
import csv
import collections
import re
import io
import json
import xml.etree.ElementTree as ET
import requests
import pandas
import pubchempy as p


#--------------------CODE2----------------------------
#For finding the mapping between drugbank and pubchem

INPUT_PATH1 = "/home/16AT72P01/Excelra/Drugbank/drugChemicalKey.tsv" 
OUTPUT_PATH1 = "/home/16AT72P01/Excelra/Drugbank/drugChemical.tsv" 
drugbank_df1 = pandas.read_table(INPUT_PATH1)
drugbank_df1 = drugbank_df1[-drugbank_df1.inchi.isnull()]

#print(drugbank_df1)

# map DrugBank compounds to pubchem using InChI 
rows = list()
for i, row in drugbank_df1.iterrows():
    try:
        compounds = p.get_compounds(row.inchi,namespace='inchi')
    except p.BadRequestError:
        print('BadRequestError', row)
        continue
    try:
        compound, = compounds
    except ValueError:
        print(row, compounds)
        continue
    row['PUBCHEM_CID'] = compound.cid
    a = compound.cid
    if(a):
    	c = p.Compound.from_cid(a)
    	row['MOLECULAR_FORMULA'] = c.molecular_formula
    	row["MOLECULAR_WEIGHT"] = c.molecular_weight
    	row["ISOMERIC_SMILES"] = c.isomeric_smiles
    	row["XLOGP"] = c.xlogp
    	row["IUPAC_NAME"] = c.iupac_name
    	row["SYNONYM"] = c.synonyms
    	#row["MOLECULAR_STRUCTURE"] = c.to_dict(properties=['atoms', 'bonds', 'inchi'])

    rows.append(row)
    print(rows)

# Create a DataFrame of the mapping
mapped_df = pandas.DataFrame(rows)
mapping_df = mapped_df[['DID','PUBCHEM_CID','MOLECULAR_FORMULA',"MOLECULAR_WEIGHT","ISOMERIC_SMILES","XLOGP","IUPAC_NAME","SYNONYM"]].dropna()
mapping_df.head()

# Save mapping
mapping_df.to_csv(OUTPUT_PATH1, index=False, sep='\t')

# The number of DrugBank compounds that did not uniquely map to PubChem
print(len(drugbank_df) - len(mapping_df))
