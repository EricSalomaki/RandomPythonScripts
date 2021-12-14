import sys
from Bio import SeqIO

renaming = sys.argv[1]
infile = open(renaming)
lines = infile.read()
infile.close()

fas = sys.argv[2]
infasta = SeqIO.parse(fas, "fasta")

outfile = sys.argv[3]

lines=lines.split('\n') #split on return
lines=[line for line in lines if line.strip() !=""] #remove empty lines

name_d = {}
for line in lines:
	old = line.split('\t')[0]
	new = line.split('\t')[1]
	name_d[old] = new
new_d = {}

for record in infasta:
	n = record.id
	s = record.seq
	if n not in name_d:
		new_d[n] = record
	else:
		for k,v in name_d.items():
			if k == n:
				record.id = v
				record.description = v
				new_d[n] = record

with open(outfile, "w") as renamed:
	SeqIO.write(new_d.values(), renamed, "fasta")

			
