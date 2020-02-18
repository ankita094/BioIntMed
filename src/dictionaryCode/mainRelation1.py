#create the relation file for various drug-drug interaction data
#Python 3.6.5 |Anaconda, Inc.

import sys
import csv
csv.field_size_limit(sys.maxsize)
import spacy

#location of the input files
INPUT_PATH = "/home/16AT72P01/Excelra/Drugbank/Relation/"
fileLoc1 = INPUT_PATH + "drugInteractionRel.csv"
with open("/home/16AT72P01/Excelra/Drugbank/Relation/drugInteractionRel2.csv","w") as wr:
	wr.write("DID1"+"\t"+"DrugName1"+"\t"+"DID2"+"\t"+"DrugName2"+"\t"+"Modulate"+"\t"+"FunctionalComponent"+"\t"+"Description"+"\n")
	
	c=c1=c2=c3=c4=c5=c6=c7=c8=c9=c10=c11=c12=c13=c14=c16=c17=c18=c19=c20=c21=c22=c23=c24=c25=c26=c27=c28=c29=c30=c31=c32=c33=\
	c34=c35=c36=c37=c38=c39=c40=c41=c42=c43=c44=c45=c46=c47=c48=c49=c50=c51=c52=c53=c54=c55=c56=c57=c58=c59=c60=c61=0
	nlp = spacy.load('en')
	with open(fileLoc1) as csvfile:
	        reader = csv.DictReader(csvfile, delimiter='\t')
	        for row in reader:
	            #print(row)
	            sentence=row['drug-interactions.drug-interaction.description']

	            if "absorption" in sentence:
	            	c=c+1
	            	value ="absorption"
	            elif "effectiveness" in sentence:
	            	c1=c1+1
	            	value ="effectiveness"
	            elif "risk of a hypersensitivity reaction to Ioxilan" in sentence:
	            	c2=c2+1
	            	value ="risk of a hypersensitivity reaction to Ioxilan"
	            elif "risk or severity of hypotension and neuromuscular blockade" in sentence:
	            	c3=c3+1
	            	value ="risk or severity of hypotension and neuromuscular blockade"
	            elif "risk or severity of hypotension, conduction block, and bradycardia" in sentence:
	            	c4=c4+1
	            	value ="risk or severity of hypotension, conduction block, and bradycardia"
	            elif "risk or severity of hypotension, nitritoid reactions, facial flushing, nausea, and vomiting" in sentence:
	            	c5=c5+1
	            	value ="risk or severity of hypotension, nitritoid reactions, facial flushing, nausea, and vomiting"
	            elif "risk or severity of angioedema" in sentence:
	            	c6=c6+1
	            	value ="risk or severity of angioedema"
	            elif "risk or severity of infection" in sentence:
	            	c7=c7+1
	            	value ="risk or severity of infection"
	            elif "risk or severity of rhabdomyolysis" in sentence:
	            	c8=c8+1
	            	value ="risk or severity of rhabdomyolysis"
	            elif "risk or severity of renal failure and hyperkalemia" in sentence:
	            	c9=c9+1
	            	value ="risk or severity of renal failure and hyperkalemia"
	            elif "risk or severity of ventricular arrhythmias" in sentence:
	            	c10=c10+1
	            	value ="risk or severity of ventricular arrhythmias"
	            elif "risk or severity of anemia and severe leukopenia" in sentence:
	            	c11=c11+1
	            	value ="risk or severity of anemia and severe leukopenia"
	            elif "risk or severity of severe leukopenia" in sentence:
	            	c12=c12+1
	            	value ="risk or severity of severe leukopenia"
	            elif "risk of a hypersensitivity reaction" in sentence:
	            	c13=c13+1
	            	value ="risk of a hypersensitivity reaction"
	            elif "risk or severity of hyperkalemia" in sentence:
	            	c14=c14+1
	            	value ="risk or severity of hyperkalemia"
	            elif "risk or severity of renal failure" in sentence:
	            	c16=c16+1
	            	value ="risk or severity of renal failure"
	            elif "bioavailability" in sentence:
	            	c17=c17+1
	            	value ="bioavailability"
	            elif "risk or severity of serotonin syndrome" in sentence:
	            	c18=c18+1
	            	value ="risk or severity of serotonin syndrome"
	            elif "risk or severity of convulsion" in sentence:
	            	c19=c19+1
	            	value ="risk or severity of convulsion"
	            elif "risk or severity of hypertension" in sentence:
	            	c20=c20+1
	            	value ="risk or severity of hypertension"
	            elif "risk or severity of sedation" in sentence:
	            	c21=c21+1
	            	value ="risk or severity of sedation"
	            elif "risk or severity of thrombotic microangiopathy" in sentence:
	            	c22=c22+1
	            	value ="risk or severity of thrombotic microangiopathy"
	            elif "risk or severity of hypercoagulability" in sentence:
	            	c23=c23+1
	            	value ="risk or severity of hypercoagulability"
	            elif "risk or severity of cytotoxicity" in sentence:
	            	c24=c24+1
	            	value ="risk or severity of cytotoxicity"
	            elif "risk or severity of QTc prolongation" in sentence:
	            	c25=c25+1
	            	value ="risk or severity of QTc prolongation"
	            elif "risk or severity of edema formation" in sentence:
	            	c26=c26+1
	            	value ="risk or severity of edema formation"
	            elif "risk or severity of fluid retention" in sentence:
	            	c27=c27+1
	            	value ="risk or severity of fluid retention"
	            elif "risk or severity of adverse effects" in sentence:
	            	c28=c28+1
	            	value ="risk or severity of adverse effects"
	            elif "risk or severity of hypotension" in sentence:
	             	c29=c29+1
	             	value ="risk or severity of hypotension"
	            elif "excretion rate" in sentence:
	            	c30=c30+1
	            	value ="excretion rate"
	            elif "metabolism" in sentence:
	             	c31=c31+1
	             	value ="metabolism"
	            elif "activities" in sentence:
	            	c32=c32+1
	            	l=sentence.split(" ")
	            	i=l.index("activities")

	            	value =str(l[i-1])+" "+str(l[i])
	            elif "therapeutic efficacy" in sentence:
	            	c33=c33+1
	            	value ="therapeutic efficacy"
	            elif "serum concentration of the active metabolites" in sentence and "loss in efficacy" in sentence:
	            	print("yes")
	            	c61=c61+1
	            	value ="serum concentration of the active metabolites,efficacy"
	            elif "serum concentration of the active metabolites" in sentence:
	            	c34=c34+1
	            	value ="serum concentration of the active metabolites"
	            elif "risk or severity of bleeding" in sentence:
	            	c35=c35+1
	            	value ="risk or severity of bleeding"
	            elif "risk or severity of hyponatremia" in sentence:
	            	c36=c36+1
	            	value ="risk or severity of hyponatremia"
	            elif "risk or severity of heart failure" in sentence:
	            	c37=c37+1
	            	value ="risk or severity of heart failure"
	            elif "risk or severity of congestive heart failure and hypotension" in sentence:
	            	c38=c38+1
	            	value ="risk or severity of congestive heart failure and hypotension"
	            elif "excretion" in sentence:
	            	c39=c39+1
	            	value ="excretion"
	            elif "protein binding" in sentence:
	             	c40=c40+1
	             	value ="protein binding"
	            elif "severity of myelosuppression" in sentence:
	            	c41=c41+1
	            	value ="severity of myelosuppression"
	            elif "risk or severity of myelosuppression" in sentence:
	             	c42=c42+1
	             	value ="risk or severity of myelosuppression"
	            elif "risk or severity of hypokalemia" in sentence:
	            	c43=c43+1
	            	value ="risk or severity of hypokalemia"
	            elif "risk or severity of myopathy and rhabdomyolysis" in sentence:
	            	c44=c44+1
	            	value ="risk or severity of myopathy and rhabdomyolysis"
	            elif "risk or severity of myocardial ischemia" in sentence:
	            	c45=c45+1
	            	value ="risk or severity of myocardial ischemia"
	            elif "risk or severity of hemorrhage" in sentence:
	            	c46=c46+1
	            	value ="risk or severity of hemorrhage"
	            elif "risk or severity of increased glucose" in sentence:
	            	c47=c47+1
	            	value ="risk or severity of increased glucose"
	            elif "risk or severity of ototoxicity and nephrotoxicity" in sentence:
	            	c48=c48+1
	            	value ="risk or severity of ototoxicity and nephrotoxicity"
	            elif "risk or severity of myopathy, rhabdomyolysis, and myoglobinuria" in sentence:
	            	c49=c49+1
	            	value ="risk or severity of myopathy, rhabdomyolysis, and myoglobinuria"
	            elif "risk or severity of generalized seizure and bradycardia" in sentence:
	             	c50=c50+1
	             	value ="risk or severity of generalized seizure and bradycardia"
	            elif "risk or severity of bradycardia" in sentence:
	            	c51=c51+1
	            	value ="risk or severity of bradycardia"
	            elif "risk or severity of increased transaminases" in sentence:
	             	c52=c52+1
	             	value ="risk or severity of increased transaminases"
	            elif "risk or severity of myopathy, rhabdomyolysis, and myoglobinuria" in sentence:
	            	c53=c53+1
	            	value ="risk or severity of myopathy, rhabdomyolysis, and myoglobinuria"
	            elif "risk or severity of myopathy" in sentence:
	            	c54=c54+1
	            	value ="risk or severity of myopathy"
	            elif "risk or severity of sinus node depression" in sentence:
	            	c55=c55+1
	            	value = "risk or severity of sinus node depression"
	            elif "risk or severity of pulmonary toxicity" in sentence:
	            	c56=c56+1
	            	value ="risk or severity of pulmonary toxicity"
	            elif "risk or severity of intraocular pressure" in sentence:
	            	c57=c57+1
	            	value ="risk or severity of intraocular pressure"
	            elif "risk or severity of weight gain" in sentence:
	            	c58=c58+1
	            	value = "risk or severity of weight gain"
	            elif "risk or severity of generalized seizure" in sentence:
	            	c59=c59+1
	            	value = "risk or severity of generalized seizure"
	            elif "serum concentration" in sentence:
	            	c60=c60+1
	            	value = "serum concentration"
	            else:
	            	print(sentence)

	            index1=row['drug-interactions.drug-interaction.drugbank-id']
	            entity1=row['drug-interactions.drug-interaction.name']
	            index2=row['drugbank-id._VALUE[0]']
	            entity2=row['name']
	            sentence=row['drug-interactions.drug-interaction.description']
	            pos1 = sentence.find(entity1)
	            pos2 = sentence.find(entity2)


	            if 'decreased' in sentence:
	            	if pos1<pos2:
	            		wr.write(index2+"\t"+entity2+"\t"+index1+"\t"+entity1+"\t"+"decrease"+"\t"+value+"\t"+sentence+"\n")
	            	else:
	            		wr.write(index1+"\t"+entity1+"\t"+index2+"\t"+entity2+"\t"+"decrease"+"\t"+value+"\t"+sentence+"\n")
	            elif 'increased' in sentence:
	            	if pos1<pos2:
	            		wr.write(index2+"\t"+entity2+"\t"+index1+"\t"+entity1+"\t"+"increase"+"\t"+value+"\t"+sentence+"\n")
	            	else:
	            		wr.write(index1+"\t"+entity1+"\t"+index2+"\t"+entity2+"\t"+"increase"+"\t"+value+"\t"+sentence+"\n")
	            elif 'decrease' in sentence:
	            		if pos1<pos2:
	            			wr.write(index1+"\t"+entity1+"\t"+index2+"\t"+entity2+"\t"+"decrease"+"\t"+value+"\t"+sentence+"\n")
	            		else:
	            			wr.write(index2+"\t"+entity2+"\t"+index1+"\t"+entity1+"\t"+"decrease"+"\t"+value+"\t"+sentence+"\n")
	            elif 'increase' in sentence:
	            	if pos1<pos2:
	            		wr.write(index1+"\t"+entity1+"\t"+index2+"\t"+entity2+"\t"+"increase"+"\t"+value+"\t"+sentence+"\n")
	            	else:
	            		wr.write(index2+"\t"+entity2+"\t"+index1+"\t"+entity1+"\t"+"increase"+"\t"+value+"\t"+sentence+"\n")

	            elif 'reduced' in sentence:
	            	if pos1<pos2:
	            		wr.write(index2+"\t"+entity2+"\t"+index1+"\t"+entity1+"\t"+"reduce"+"\t"+value+"\t"+sentence+"\n")
	            	else:
	            		wr.write(index1+"\t"+entity1+"\t"+index2+"\t"+entity2+"\t"+"reduce"+"\t"+value+"\t"+sentence+"\n")

	            else:
 	            	check = -1
 	            	print(sentence)

	        print(c+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+\
	        	c34+c35+c36+c37+c38+c39+c40+c41+c42+c43+c44+c45+c46+c47+c48+c49+c50+c51+c52+c53+c54+c55+c56+c57+c58+c59+c60+c61)
	       
	            
           