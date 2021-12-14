import sys
from Bio import SeqIO
import csv
import os
import glob

print('Required input: 1) Reciprocal blast output file; 2) Reciprocal blast query fasta; 3) Path to directory containing orthogroup fastas') 

def recip_blast_parser(blastout, fas):

	infas = SeqIO.parse(fas, "fasta")
	
	infile = open(blastout, 'r')
	lines = infile.read()
	infile.close()
	
	lines = lines.split('\n')
	lines=[line for line in lines if line.strip() !=""] #remove empty lines
	
	blast_d = {}
	gene = blastout.split('.')[0]
	keep = []
	
	for line in lines:
		if line.split('\t')[0] in blast_d:
			pass
		else:
			blast_d[line.split('\t')[0]] = line.split('\t')
			
	for k,v in blast_d.items():
		hit = v[1]
		hit = hit.split('+')[0]
		#print(hit)
		if hit == gene:
			keep.append(k)
		else:
			pass
	num_kept = (len(keep))
	
	print(num_kept)
	return keep, num_kept
	
def find_OGs(keeplist, fas):
	directory = sys.argv[3]
	files = [fname for fname in glob.glob(directory + '*.fa')]
	OGs = []	
	
	for fname in files:											#iterate though all files
		with open(fname) as OG_fas:	
			for record in SeqIO.parse(OG_fas, "fasta"):
				h = keeplist[0]
				for l in h:
					if record.id == l:
						OGs.append(fname.split('/')[-1])					
					else:
						pass
	OGname = [] 
	for name in OGs:
		if name.split('.')[0] in OGname:
			pass
		else:
			OGname.append(name.split('.')[0])
	mergeOGs = set(OGs)
	fasoutname = "MergedOGs/" + fas.split('.')[0] + ".fasta"
	OGoutname = "MergedOGs/" + fas.split('.')[0] + ".txt"
	os.makedirs(os.path.dirname(fasoutname), exist_ok=True)
	print(fasoutname)
	print(OGname)
	mergeOGs_paths = []
	for OG in mergeOGs:
		mergeOGs_paths.append(directory + OG)
	with open(fasoutname, 'w') as out:
		for file in mergeOGs_paths:
			with open(file) as ins:
				out.write(ins.read())
			out.write('\n')
	with open(OGoutname, 'w') as OGout:
		for orthogroup in OGname:
			OGout.write(orthogroup + '\n')



def main():
	blastout = sys.argv[1]
	fas = sys.argv[2]
	keeplist = recip_blast_parser(blastout, fas)
	find_OGs(keeplist, fas)

if __name__ == '__main__':
	main()
