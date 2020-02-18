#CODE9---To estimate clinical trial-phase details----
#Python 3.6.5 |Anaconda, Inc.

import csv

phase0 = set()
phase1 = set()
phase12 = set()
phase2 = set()
phase23 = set()
phase3 = set()
phase4 = set()
other = set()

inputFileName1 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/mainClinical1.csv"
outputFileName1 = "/home/16AT72P01/EstimateFile/CLINICALOUTPUT/phaseTrial.csv"

with open(outputFileName1,"w",encoding='utf8') as csv_file:
	writer = csv.writer(csv_file,delimiter='\t')
	writer.writerow(["phase","countTrials"])
	with open(inputFileName1,"r",encoding='utf8') as csv_file1:
	  			reader = csv.DictReader(csv_file1,delimiter ="\t")
	  			for row in reader:
	  				if(row['phase'] == "Early Phase 1"):
	  					phase0.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 1"):
	  					phase1.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 2"):
	  					phase2.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 1/Phase 2"):
	  					phase12.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 2/Phase 3"):
	  					phase23.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 3"):
	  					phase3.add(row['clinical_id'])
	  				elif(row['phase'] == "Phase 4"):
	  					phase4.add(row['clinical_id'])
	  				else:
	  					print(row['phase'])
	  					other.add(row['clinical_id'])
	  				print("-----------------")
	csv_file1.close()
	writer.writerow(["Phase 0",len(phase0)])
	writer.writerow(["Phase 1",len(phase1)])
	writer.writerow(["Phase 1/2",len(phase12)])
	writer.writerow(["Phase 2",len(phase2)])
	writer.writerow(["Phase 2/3",len(phase23)])
	writer.writerow(["Phase 3",len(phase3)])
	writer.writerow(["Phase 4",len(phase4)])
	writer.writerow(["other",len(other)])

csv_file.close()
