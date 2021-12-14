import sys
from Bio import SeqIO

alnfile = sys.argv[1]
filter_percent = sys.argv[2]

alignment=SeqIO.parse(open(alnfile), 'fasta')

removed_sequences=[]
with open(alnfile + '.len_filtered', 'w') as keep:
    for record in alignment:
        name, sequence = record.id, str(record.seq)
        coverage = len(str(record.seq).replace('-', '')) / len(record.seq)
        if coverage > float(filter_percent)/100:
            keep.write(f'>{record.description}_{round(coverage, 2)}\n{record.seq}\n')
        else:
            print(record.name, alnfile)
            removed_sequences.append(f'>{record.description}_{round(coverage, 2)}\n{record.seq}\n')

with open(alnfile + '.removed', 'w') as removed:            
    for record in removed_sequences:
        removed.write(record)
