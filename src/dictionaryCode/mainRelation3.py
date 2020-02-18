#To extract the target and drug-target relation from drugbank datasets
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


OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/Relation/drugTargetRelation4.tsv"
#INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/fulldatabase.xml" 
INPUT_PATH = 'sampleData/dictionaryExample/DrugbankExampleData.xml'

with open(INPUT_PATH) as xml_file1:
    tree = ET.parse(xml_file1)
root = tree.getroot()

ls = '{http://www.drugbank.ca}'

protein_rows = list()
for i, drug in enumerate(root):
    drugbank_id = drug.findtext(ls + "drugbank-id[@primary='true']")
    drugname = drug.findtext(ls + "name")
    for category in ['target', 'enzyme', 'carrier', 'transporter']:
        proteins = drug.findall('{ls}{at}s/{ls}{at}'.format(ls=ls, at=category))
        for protein in proteins:
            row = {'DID': drugbank_id, 'CATEGORY': category, 'DRUGNAME': drugname}
            row['TARGET_ID'] = protein.findtext('{}id'.format(ls))
            row['TARGET_NAME'] = protein.findtext('{}name'.format(ls))
            actions = protein.findall('{ls}actions/{ls}action'.format(ls=ls))
            row['ACTION'] = '|'.join(action.text for action in actions)
            uniprot_ids = [polypep.text for polypep in protein.findall(
                "{ls}polypeptide/{ls}external-identifiers/{ls}external-identifier[{ls}resource='UniProtKB']/{ls}identifier".format(ls=ls))]            
            if len(uniprot_ids) != 1:
                continue
            row['UNIPROT_ID'] = uniprot_ids[0]
            row['SYNONYMS'] = '|'.join(polypep1.text for polypep1 in protein.findall(
                "{ls}polypeptide/{ls}synonyms/{ls}synonym".format(ls=ls)))
            protein_rows.append(row)
            #print(row)


columns = ['DID','DRUGNAME','CATEGORY','TARGET_ID','TARGET_NAME','UNIPROT_ID','SYNONYMS','ACTION']

protein_df = pandas.DataFrame.from_dict(protein_rows)[columns]
protein_df.drop_duplicates(subset=["TARGET_ID","TARGET_NAME"], keep='last')
print(protein_df)
protein_df.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')
