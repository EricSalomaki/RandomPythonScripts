import sys
import os
from Bio import SeqIO

matchfile = sys.argv[1]
infile = open(matchfile)
lines = infile.read()
infile.close

lines=lines.split('\n') #split on return
lines=[line for line in lines if line.strip() !=""] #remove empty lines

match={}
for i in lines: 
	match[i.split('\t')[0]]=i

for i in match: #Iterate through matches
	jan=match[i].split('\t')[1] + '.final.fas'
	burk=match[i].split('\t')[0] + '.final.fas'

	greg_d = {'Gregarina_sp_Pseudo_7':'Gregarina_sp_Pseudo', 'Gregarina_sp_Pseudo_8':'Gregarina_sp_Pseudo', 'Gregarina_sp_Pseudo_9':'Gregarina_sp_Pseudo','Gregarina_sp_Poly_1_total':'Gregarina_sp_Poly', 'Gregarina_sp_Poly_29':'Gregarina_sp_Poly', 'Gregarina_sp_Poly_39':'Gregarina_sp_Poly', 'Protomagalhaensia_sp_Gyna_25':'Protomagalhaensia_sp_Gyna', 'Protomagalhaensia_sp_Gyna_26':'Protomagalhaensia_sp_Gyna', 'Protomagalhaensia_wolfi_75':'Protomagalhaensia_wolfi', 'Protomagalhaensia_wolfi_77':'Protomagalhaensia_wolfi', 'Protomagalhaensia_wolfi_80':'Protomagalhaensia_wolfi', 'Blabericola_migrator_1_total':'Blabericola_migrator', 'Blabericola_migrator_2_total':'Blabericola_migrator'}

	burki = SeqIO.parse(burk, "fasta") #Parse burki fasta
	janou = SeqIO.parse(jan, "fasta") #Parse Jan fasta
	
	burki_d = {} #create empty dictionary that will be filled with the burki data  

	for i in burki: # iterate through burki fasta
		bh = i.id #assign fasta header as bh
		bs = i.seq #assign sequence as bs
		bhr = bh.split('__')[0] #remove the contig ID info from bh
		if bhr not in greg_d: #iterate through the keys/values in gregarine renaming dictionary
			burki_d[bhr]=i #add jhr as key to burki_d and add the entire record as values
		else:
			for k,v in greg_d.items():
				if k == bhr:
					bhr=v
			#print (bhr)
			burki_d[bhr] = i #add the unmodified bh as merged dictionary key and the initial fasta header (with contig ID) and sequence to the dictioanry as values 
	for i in janou: #iterate through jan fasta
		jh = i.id #assign fasta header as jh
		js = i.seq #assign sequence as js
		jhr = jh.split('__')[0]  #remove the contig ID info from jh to name jhr
		if jhr in burki_d:
			pass
		else:
			if jhr not in greg_d:
				burki_d[jhr]=i #add jhr as key to burki_d and add the entire record as values
			else:
				for k2,v2 in greg_d.items(): #iterate through keys and values in greg renaming dictionary
					if jhr == k2: # if the jan fasta header is in greg_d renaming dictionary
						jhr=v2 # renane jh with the value from greg dictionary
						burki_d[jhr] = i #assign record to key jhr
	with open(jan+".merged.fas", "w") as merged:
		SeqIO.write(burki_d.values(), merged, "fasta")


