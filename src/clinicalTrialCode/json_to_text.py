#sample code to read a json file and write it into text file
#Python 3.6.5 |Anaconda, Inc.

import json

with open('Final_abstract.json') as json_data:
    d = json.load(json_data)
    print(d)
    
    
    total_words=0
    total_words=total_words + len(d)
    print('value=%d' %total_words)
    
    
    f = open("json_to_text.txt", "a")
    
    for i in range(len(d)) :
        a = json.dumps(d[i]['org_study_id']['0'])
        b = json.dumps(d[i]['nct_id']['0'])
        c = json.dumps(d[i]['brief_title']['0'])
        e = json.dumps(d[i]['brief_summary']['0'])
        g = json.dumps(d[i]['detailed_description']['0'])
        
        value = b + '\t' + c + e + g + '\n'
        f.write(value)
        print ("value %s %s %s %s %s " % (a,b,c,e,g))
       

    
