import sys
import os
from Bio import SeqIO

#read fasta file 
fa=SeqIO.parse(open(sys.argv[1]), 'fasta')
print(sys.argv[1])
name = sys.argv[1].rsplit('.', 1)[0]
GTF=[]
for record in fa:
    stop = str(len(record.seq))
    seq = record.name
    GTF.append(seq + "\t" + "gtf_from_fasta" + "\t" + "CDS" + "\t" +str(1) + "\t" + stop + "\t" + "." + "\t" + "+" + "\t" + "." +"\t"+ 'gene_id "' + seq +'"'  + '; transcript_id "' + seq +'"'  + '; exon_number 1' + ";\n" + seq + "\t" + "gtf_from_fasta" + "\t" + "exon" + "\t" +str(1) + "\t" + stop + "\t" + "." + "\t" + "+" + "\t" + "." +"\t" + 'gene_id "' + seq +'"'  + '; transcript_id "' + seq +'"'  + '; exon_number 1' + ";\n")

with open(name + '.gtf', 'w') as gtf_out:
    for i in GTF:
        print(i)
        gtf_out.write(i)
