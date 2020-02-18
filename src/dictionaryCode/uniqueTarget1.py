#To extract the target and drug-target relation from drugbank datasets to create unique list of target name for DrugBank dictionary
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


OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/TARGETTABLE1.tsv"
#INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/fulldatabase.xml" 
INPUT_PATH = 'sampleData/dictionaryExample/DrugbankExampleData.xml'


#We need to know the schema of the xml file before executing the script
with open(INPUT_PATH) as xml_file1:
    tree = ET.parse(xml_file1)
root = tree.getroot()
ls = '{http://www.drugbank.ca}'

protein_rows = list()
for i, drug in enumerate(root):
    drugbank_id = drug.findtext(ls + "drugbank-id[@primary='true']")
    for category in ['target', 'enzyme', 'carrier', 'transporter']:
        proteins = drug.findall('{ls}{at}s/{ls}{at}'.format(ls=ls, at=category))
        for protein in proteins:
            row = {'CATEGORY': category}
            row['TARGET_ID'] = protein.findtext('{}id'.format(ls))
            row['TARGET_NAME'] = protein.findtext('{}name'.format(ls))
            row['ORGANISM'] = protein.findtext('{}organism'.format(ls))
            row['KNOWN_ACTION'] = protein.findtext('{}known-action'.format(ls))
            actions = protein.findall('{ls}actions/{ls}action'.format(ls=ls))
            row['ACTION'] = '|'.join(action.text for action in actions)
            uniprot_ids = [polypep.text for polypep in protein.findall(
                "{ls}polypeptide/{ls}external-identifiers/{ls}external-identifier[{ls}resource='UniProtKB']/{ls}identifier".format(ls=ls))]            
            if len(uniprot_ids) != 1:
                continue
            row['UNIPROT_ID'] = uniprot_ids[0]
            row['SYNONYMS'] = '|'.join(polypep1.text for polypep1 in protein.findall(
                "{ls}polypeptide/{ls}synonyms/{ls}synonym".format(ls=ls)))

            row['GO_CLASSIFICATION_FUNCTION'] = '|'.join(polypep3.text for polypep3 in protein.findall(
            	"{ls}polypeptide/{ls}go-classifiers/{ls}go-classifier/[{ls}category='function']/{ls}description".format(ls=ls)))

            row['GO_CLASSIFICATION_PROCESS'] = '|'.join(polypep3.text for polypep3 in protein.findall(
            	"{ls}polypeptide/{ls}go-classifiers/{ls}go-classifier/[{ls}category='process']/{ls}description".format(ls=ls)))



            for polypep2 in protein.findall("{ls}polypeptide".format(ls=ls)): 
	            row['LOCUS'] = polypep2.findtext('{}locus'.format(ls))
	            row['CELLULAR_LOCATION'] = polypep2.findtext('{}cellular-location'.format(ls))
	            row['SIGNAL_REGION'] = polypep2.findtext('{}signal-regions'.format(ls))
	            row['THEORITICAL_PI'] = polypep2.findtext('{}theoretical-pi'.format(ls))
	            row['MOLECULAR_WEIGHT'] = polypep2.findtext('{}molecular-weight'.format(ls))
	            row['CHROMOSOME_LOCATION'] = polypep2.findtext('{}chromosome-location'.format(ls))
	            row['GENE_SEQUENCE'] = polypep2.findtext('{}gene-sequence'.format(ls))
	            row['AMINOACID_SEQUENCE'] = polypep2.findtext('{}amino-acid-sequence'.format(ls))
	            row['GENERAL_FUNCTION'] = polypep2.findtext('{}general-function'.format(ls))
	            row['SPECIFIC_FUNCTION'] = polypep2.findtext('{}specific-function'.format(ls))
            protein_rows.append(row)
            #print(row)


columns = ['CATEGORY','TARGET_ID','UNIPROT_ID','TARGET_NAME','SYNONYMS','ORGANISM','KNOWN_ACTION','ACTION','GO_CLASSIFICATION_FUNCTION',\
        'GO_CLASSIFICATION_PROCESS','GENERAL_FUNCTION','SPECIFIC_FUNCTION','LOCUS','CELLULAR_LOCATION','SIGNAL_REGION','THEORITICAL_PI','MOLECULAR_WEIGHT',\
        'CHROMOSOME_LOCATION','GENE_SEQUENCE','AMINOACID_SEQUENCE']


protein_df = pandas.DataFrame.from_dict(protein_rows)[columns]
protein_df.drop_duplicates(subset=["CATEGORY","TARGET_ID","TARGET_NAME"],keep="first",inplace=True)
print(protein_df)
protein_df.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')
