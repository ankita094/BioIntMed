##---------------Convert the filtered XML file to JSON format for clinical trails--------------
#Python 3.6.5 |Anaconda, Inc.

import json
import xmltodict
import io
import os
import glob

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def convertToJson(xml_file, xml_attribs=True):
    name=xml_file
    print(name)
    print("yes")
    with open(xml_file, "rb") as f: 
 
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        value = json.dumps(d, indent=4)
        print(".............")
        file11 = str(name).strip('/').split('/')[-1:][0]
        print(file11)
        a = str(file11).strip('.').split('.')[:1][0]
        print(a)
        new_file = "/home/CLINICALOUTPUT/clinicaljson/"+a+".json"
        print(new_file)
        with io.open(new_file, 'w', encoding='utf8') as outfile:
         outfile.write(to_unicode(value))


def getTopic(val):
 print(val)
 xml_file1 = val
 print(xml_file1)
 convertToJson(xml_file1)


def generateRequiredJSON(path):
 for files1 in glob.glob(os.path.join(path, '*.xml')):
    getTopic(files1)


path = 'sampleData/clinicalExample/'
generateRequiredJSON(path)



