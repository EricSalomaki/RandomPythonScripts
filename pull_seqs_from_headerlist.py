import sys
from Bio import SeqIO

blastout = sys.argv[1]
master_fas = sys.argv[2]
outfas = sys.argv[3]

infas = SeqIO.parse(master_fas, "fasta")

infile = open(blastout, 'r')
lines = infile.read()
infile.close()

lines = lines.split('\n')
lines=[line for line in lines if line.strip() !=""] #remove empty lines

keep = []

for line in lines:
	if line.split('\t')[1] in keep:
		pass
	else:
		keep.append(line.split('\t')[1])


					
with open(outfas, 'w') as out:
	for record in infas:
		for i in keep:
			if i == record.id:
				SeqIO.write(record,out,'fasta')
				print(record.id)
			else:
				pass
