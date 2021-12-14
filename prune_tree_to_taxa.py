import os
import sys
import glob
from Bio import Phylo

fname = open(sys.argv[1])
line = fname.read()
fname.close()

seqs = line.split('>')[1:]
names_aln = []
for seq in seqs:
    names_aln.append(seq.split('\n')[0])

tree = Phylo.read(sys.argv[2], "newick")

names_tree = tree.get_terminals()
print(names_tree)
names_all = []
for i in names_tree:
    names_all.append(i.name)
print(names_all)
names_to_remove = set(names_all) - set(names_aln)

print(names_to_remove)

for name in names_to_remove:
    print(name)
    tree.prune(name)

Phylo.write(tree, 'temp.treeee', "newick")
infile = open('temp.treeee')
line = infile.read()
infile.close()

os.system('rm temp.treeee')
out = open(sys.argv[3],'w')
out.write(line.replace(':0.00000',''))
out.close()