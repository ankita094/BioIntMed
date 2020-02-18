#To extract the chemical property and map those to pubChem database to extract multiple features or chemical properties script 1
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

#--------------CODE1-------------------
#For creating the drugid and inchi file

OUTPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/drugChemicalKey.tsv" 
#INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/fulldatabase.xml" 
INPUT_PATH = 'sampleData/dictionaryExample/DrugbankExampleData.xml'


with open(INPUT_PATH) as xml_file1:
    tree = ET.parse(xml_file1)
root = tree.getroot()

ls = '{http://www.drugbank.ca}'

inchikey_value = "{ls}calculated-properties/{ls}property[{ls}kind='InChIKey']/{ls}value"
inchi_value = "{ls}calculated-properties/{ls}property[{ls}kind='InChI']/{ls}value"
rows = list()
for i, drug in enumerate(root):
    row = collections.OrderedDict()
    assert drug.tag == ls + 'drug'
    row['DID'] = drug.findtext(ls + "drugbank-id[@primary='true']")
    row['DRUG_NAME'] = drug.findtext(ls + "name")
    row['inchi'] = drug.findtext(inchi_value.format(ls = ls))
    row['INCHIKEY'] = drug.findtext(inchikey_value.format(ls = ls))

    rows.append(row)
    columns = ['DID','DRUG_NAME','inchi','INCHIKEY']

drugbank_df = pandas.DataFrame.from_dict(rows)[columns]
drugbank_df.head()

drugbank_df.to_csv(OUTPUT_PATH,sep='\t',index=False,encoding='utf-8')

