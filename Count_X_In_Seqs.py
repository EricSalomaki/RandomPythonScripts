import csv
import sys
from Bio import SeqIO


alnfile1 = sys.argv[1]
alnfile2 = sys.argv[2]

alignment1=SeqIO.parse(open(alnfile1), 'fasta')
alignment2=SeqIO.parse(open(alnfile2), 'fasta')

aln1_dict={}
aln2_dict={}

for record in alignment1:
	name, sequence = record.id, str(record.seq)
	X1_count = 0
	X1_count += record.seq.count('X')
	X1_percent = X1_count/len(sequence)
	aln1_dict.update({name: [len(sequence), X1_count, "{:.2f}".format(X1_percent)]})

for record in alignment2:
	name, sequence = record.id, str(record.seq)
	X2_count = 0
	X2_count += record.seq.count('X')
	X2_percent = X2_count/len(sequence)
	aln2_dict.update({name: [len(sequence), X2_count, "{:.2f}".format(X2_percent)]})

prequal_dict =  {}
for key in (aln1_dict.keys() | aln2_dict.keys()):
    if key in aln1_dict: prequal_dict.setdefault(key, []).append(aln1_dict[key])
    if key in aln2_dict: prequal_dict.setdefault(key, []).append(aln2_dict[key])


masked = csv.writer(open(alnfile1 + ".info.csv", "w"))
for key, val in prequal_dict.items():
	masked.writerow([key, val])
