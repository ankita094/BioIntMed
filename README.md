## **BIOINTMED: Integrated Biomedical Knowledge Base with Ontologies and Clinical Trials**

### Overview :

Biomedical knowledge has a high impact on mankind and society. The work aims to integrate biomedical data from various heterogeneous sources like dictionaries or corpus and amalgamate them into an uniform accessible format for the end user like biologist, pharmacist, and data scientist. The proposed integrated biomedical knowledge base, BIOINTMED, have 11299, 12981, 4428,  61491, 48663, and 13146 unique entities for drugs, diseases, targets, genes, biomedical pathways, and adverse events, respectively. The uniform aggregated collection is also explored to study the interaction among these entity pairs.

### Code details:
<pre>
folder format:
src
|
|-clinicalTrialCode|
|                  |-clinicalIntervention|
|                  |                     |-code1.py :[1]
|                  |                     |-code2.py :[2]
|                  |                     |-code3.py :[3]
|                  |                     |-code4.py :[4]
|                  |                     |-code5.py :[5]
|                  |                     |-code6.py :[6]
|                  |                     |-code7.py :[7]
|                  |                     |-code8.py :[8]
|                  |                     |-code9.py :[9]
|                  |                     |-code10.py:[10]
|                  |
|                  |
|                  |-geneticIntervention|
|                  |                    |-code1.py :[11]
|                  |                    |-code2.py :[12]
|                  |                    |-code3.py :[13]
|                  |                    |-code4.py :[14]
|                  |                    |-code5.py :[15]
|                  |                    |-code6.py :[16]
|                  |                    |-code7.py :[17]
|                  |                    |-code8.py :[18]
|                  |                    |-code9.py :[19]
|                  |                    |-code10.py:[20]
|                  |-schemaClinical|
|                  |               |-code1.py :[21]
|                  |               |-code2.py :[22]
|                  |               |-code3.py :[23]
|                  |               |-code4.py :[24]
|                  |               |-code5.py :[25]
|                  | 
|                  |-json_to_text.py :[26]
|                  |-schema.py :[27]
|                  |-xmltojson.py :[28]
|
|-dictionaryCode|
|               |-codeAttribute|
|               |              |-code1.py :[29]
|               |              |-code2.py :[30]
|               |              |-code3.py :[31]
|               |              |-code4.py :[32]
|               |              |-code5.py :[33]
|               |              |-code6.py :[34]
|               |              |-code7.py :[35]
|               |              |-code8.py :[36]
|               |              |-code9.py :[37]
|               |              |-code10.py:[38]
|               |
|               |-others|
|                       |-CTDData1.py :[39]
|                       |-CTDData2.py :[40]
|                       |-CTDData3.py :[41]
|                       |-CTDData4.py :[42]
|                       |-CTDData5.py :[43]
|                       |-CTDData6.py :[44]
|                       |-DisGeUnique1.py :[45]
|                       |-DisGeUnique2.py :[46]
|                       |-geneData.py :[47]
|                       |-keggData2.py :[48]
|                       |-siderData1.py :[49]
|                       |-siderData2.py :[50]
|                       |-siderData3.py :[51]
|                       |-smpdbData1.py :[52]
|                       |-smpdbData2.py :[53]
|                       |-smpdbData3.py :[54]
|                       |-smpdbData4.py :[55]
|
|-countRelationInfo.py :[56]
|-DrugBankAttri.py :[57]
|-drugchemmap1.py :[58]
|-drugchemmap2.py :[59]
|-DrugName.py :[60]
|-DrugRow.py :[61]
|-mainRelation1.py :[62]
|-mainRelation2.py :[63]
|-mainRelation3.py :[64]
|-replacenull.py :[65]
|-targetxml.py :[66]
|-uniqueTarget.py :[67]
|-uniqueTarget1.py :[68]
|-XmlToCsv.py :[69]
|-XmlToJson.py :[70]
</pre>

**note** : For running the code if the script written in python run "python Filename.py" and for pyspark run "spark-submit FileName.py" in terminal. for each folder execute based on mentioned script numbers.
<pre>
[1]To filter the attribute value from clinical trial for drug invention after converting the files from xml to json
[2]To filter the attribute value from clinical trial for adverse Category and its respective counts
[3]To filter the attribute value from clinical trial for other adverse Events
[4]To filter the attribute value from clinical trial for serious adverse Events
[5]For combination serious adverse Events and other event mentioned in clinical trials
[6]To filter the attribute value from clinical trial for all conditions
[7]To filter the attribute value from clinical trial for all intervention or drug
[8]To calculate the trial frequency for drug entity
[9]To estimate clinical trial-phase details
[10]checking with the FDA approved drug from drugBank list and creating new file with FDA level
[11]To filter the file with invention type:Genetic and prepare a file list of file name
[12]Remove the set of file to another directory
[13]To filter the file with interventional study type and prepare a file list of file name
[14]Remove the set of file to another directory
[15]Convert the filtered XML file to JSON format for clinical trails
[16]To filter the file of adverse events and prepare a file list of file name
[17]To filter the attribute value from clinical trial for genetic invention
[18]To filter the attribute value from clinical trial for all intervention genetic only
[19]To estimate clinical trial-phase details
[20]To filter the attribute value from clinical trial for all conditions
[21]To filter the file with invention type:DRUG and prepare a file list of file name
[22]To filter the file with interventional study type and prepare a file list of file name
[23]To filter the file of adverse events and prepare a file list of file name
[24]To match with DRUGBANK drug list and extract the data from clinical trials
[25]To give estimation of all drug,disese,group,approved drug etc from drugBank source
[26]sample code to read a json file and write it into text file
[27]To read the schema of the clinical trial file for further analysis
[28]Convert the filtered XML file to JSON format for clinical trails
[29]To extract for drug data for the main drug table-Part extracting for main drug attribute
[30]To extract for drug data for the main drug table-For formation of classification table
[31]To extract for drug data for the main drug table-Part executing for atc code
[32]To extract for drug data for the main drug table-Part executing for drug interaction
[33]To extract for drug data for the main drug table-For preparing the data for synonyms of drug
[34]To extract for drug data for the main drug table-code to seperate out the dosages file
[35]To extract for drug data for the main drug table-code to seperate out the drug category file
[36]To extract for drug data for the main drug table-Extract the data for experimental property
[37]To extract for drug data for the main drug table-Extract gene part and its attributes
[38]To extract for drug data for the main drug table-interaction file for relation extraction part
[39]To filter human the chemical-gene interaction
[40]To filter human the unique gene information
[41]To filter human the chemical-disease interaction
[42]To filter human the gene-disease interaction
[43]To filter human the disease 
[44]code to filter human the Chemicals details 
[45]For checking unique no. of targets
[46]For calculating pathway details of metabolism
[47]To extract for gene from Homo_sapiens.gene_info data
[48]To get kegg data
[49]For preparing the list of DRUG side-effect relation from SIDER database
[50]For preparing the list of side-effect from SIDER database
[51]For preparing the list of side-effect from SIDER database
[52]First concatenating the required files into one based on the specfic attribute columns from SMPDB database and getting metabolics
[53]First concatenating the required files into one based on the specfic attribute columns from SMPDB database
[54]First concatenating the required files into one based on the specfic attribute columns from SMPDB database and protein network
[55]Consider only those row having drugbank ID The connection between drug and metabolites
[56]To count all unique relational property type in detail
[57]To extract for DrugBank drug data for attribute values
[58]To extract the chemical property and map those to pubChem database to extract multiple features or chemical properties script 1
[59]To extract the chemical property and map those to pubChem database to extract multiple features or chemical properties script 2
[60]To extract drugname and its comparison with SIDER data
[61]To prepare attribute values for drug data for experimental property done in DrugBank dataset
[62]create the relation file for various drug-drug interaction data
[63]To extract for drug action on which part physiological system by extracting the information about ATC code and considering only the first label
[64]To extract the target and drug-target relation from drugbank datasets
[65]To extract for drug data for the main drug table
[66]To extract the target feature from drugbank datasets
[67]To extract the target and drug-target relation from drugbank datasets
[68]To extract the target and drug-target relation from drugbank datasets to create unique list of target name for DrugBank dictionary
[69]To convert xml format file to json format file for DrugBank dictionary
[70]To convert xml format file to json format file for DrugBank dictionary
</pre>


### Data :

Information about the data are available from the [link](http://www.facweb.iitkgp.ac.in/~jay/BIOINTMED1/BIOINTMED.html) 

### Miscellaneous :

The overall system code will be open soon.
Please send any questions you might have about the datasets and/or codes to ankitasaha@iitkgp.ac.in

### Contact details:

Ankita Saha
Department of Advance Technology and Development Centre
Indian Institute of Technology Kharagpur
Email: ankitasaha AT iitkgp DOT ac DOT in

