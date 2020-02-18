#For retrieving some information from KEGG network files
#Python 3.6.5 |Anaconda, Inc.

import csv

with open('/home/16AT72P01/Excelra/ftp.genome.jp/pub/kegg/medicus/disease/diseasefile.csv', 'w') as wr:
	wr.write("DISEASEID"+"\t"+"DISEASE"+"\t"+"DESCRIPTION"+"\t"+"CATEGORY"+"\t"+"NETWORK"+"\t"+"GENE"+"\t"+"DRUG"+"\n")
	truevalue=0
	with open('/home/16AT72P01/Excelra/ftp.genome.jp/pub/kegg/medicus/disease/diseaseEg.txt', 'r') as g:
		
		for line in g:
		
			line1=line.split(" ")
			#print(line1[0])
			if(line1[0]=="ENTRY"):
				print("==")
				truevalue=8
				wr.write(line[6:].strip("\n").strip()+"\t"+"\t"+"\t"+"\t"+"\t"+"\t")
			elif(line1[0]=="NAME"):
				truevalue=1
				wr.write("\t"+line[5:].strip("\n").strip()+"\t"+"\t"+"\t"+"\t"+"\t")
			elif(line1[0]=="DESCRIPTION"):
				truevalue=2
				wr.write("\t"+"\t"+line[12:].strip("\n").strip()+"\t"+"\t"+"\t"+"\t")
			elif(line1[0]=="CATEGORY"):
				truevalue=3
				wr.write("\t"+"\t"+"\t"+line[9:].strip("\n").strip()+"\t"+"\t"+"\t")
			elif(line1[0]=="NETWORK"):
				truevalue=4
				wr.write("\t"+"\t"+"\t"+"\t"+line[7:].lstrip()+"\t"+"\t")
			elif(line1[0]=="GENE"):
				truevalue=5
				wr.write("\t"+"\t"+"\t"+"\t"+"\t"+line[5:].lstrip()+"\t")
			elif(line1[0]=="CARCINOGEN"):
				truevalue=0
			elif(line1[0]=="DRUG"):
				truevalue=6
				wr.write("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+line[5:].lstrip())
			elif(line1[0]=="COMMENT" or line1=="DBLINKS" or line1=="REFERENCE"):
				truevalue=0
			elif(line1[0]=="///\n"):
				truevalue=7
			else:
				if(truevalue==0):
					continue
				elif(truevalue==4):
					print("yes")
					wr.write("\t"+"\t"+"\t"+"\t"+line.lstrip("			")+"\t"+"\t")
				elif(truevalue==5):
					wr.write("\t"+"\t"+"\t"+"\t"+"\t"+line.lstrip("			")+"\t")
				elif(truevalue==6):
					wr.write("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+line.lstrip("			"))
				elif(truevalue==7):
					wr.write("\n")
				else:
					print("ok")
	g.close()
wr.close()



