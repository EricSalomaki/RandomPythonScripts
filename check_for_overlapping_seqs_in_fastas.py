import os
import sys
from Bio import SeqIO

directory = (sys.argv[1]) #PATH to Directory
filelist = []
donelist = []
mergelist = []
for filename in os.listdir(directory):
	if "fasta" in filename:
		filelist.append(directory+filename)
	else:
		pass
for file1 in filelist:
	for file2 in filelist:
		
		
		
		if file1 == file2:
			pass
		else:
			thisround = []	
			thisround.append(file1)
			thisround.append(file2)	
			thisround.sort()
			if thisround in donelist:
				pass
			else:
				donelist.append(thisround)
				total = []
				overlap = []
				with open(file1, 'r') as fa1:
					for rec1 in SeqIO.parse(fa1, "fasta"):
						total.append(rec1.id)
				with open(file2, 'r') as fa2:
					for rec2 in SeqIO.parse(fa2, "fasta"):
						if rec2.id in total:
							overlap.append(rec2.id)
						else:
							total.append(rec2.id)
				#print(len(total))
				perc_overlap = len(overlap)/len(total)*100
				if perc_overlap == 0:
					pass
				else:
					print(file1.split('/')[-1] + " and " + file2.split('/')[-1] + " share " + str(len(overlap)) + " sequences for a total of " + str("%.2f" % perc_overlap) + "%" )
