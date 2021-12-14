import os
import sys
import glob


infile = open(sys.argv[1])
line = infile.read()
infile.close()

seqs = line.split('>')[1:]
seq_d = {}

out = open(sys.argv[2],'w')
for seq in seqs:
    sequence = ''.join(seq.split('\n')[1:])
    if sequence.count('-') + sequence.count('X') + sequence.count('x') == len(sequence):
        pass
    else:
        out.write('>%s' % (seq))

out.close()




