import sys
import re
from Bio import SeqIO


alnfile = sys.argv[1]
filter_percent = sys.argv[2]

alignment=SeqIO.parse(open(alnfile), 'fasta')

removed_sequences=[]
with open(alnfile + '.motif_rich.faa', 'w') as keep:
    for record in alignment:
        name, sequence = record.id, str(record.seq)
        #print(record.seq)
        triplets = [str(record.seq)[i:i+3] for i in range(len(record.seq)-2)]
        triplets = "_".join(triplets)
        CXC_count = len(re.findall(r"C.C", triplets))
        quadruplets = [str(record.seq)[i:i+4] for i in range(len(record.seq)-3)]
        quadruplets = "_".join(quadruplets)
        CXXC_count = len(re.findall(r"C..C", quadruplets))
        print ((record.id) + ": " + (str(len(record.seq))) + " residues " + (str(CXC_count)) + " CXC " + (str(CXXC_count)) + " CXXC")
        motif_rich = CXXC_count + CXC_count
        if motif_rich > int(sys.argv[2]):
            keep.write(f">{record.description}_{CXXC_count}_{CXC_count}\n{record.seq}\n")
        else:
            #print(record.name, alnfile)
            removed_sequences.append(f">{record.description}\n{record.seq}\n")

with open(alnfile + '.not_motif_rich.faa', 'w') as removed:
    for record in removed_sequences:
        removed.write(record)
