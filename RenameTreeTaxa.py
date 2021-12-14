import sys
import os

metadatafile=sys.argv[1]
treefile=sys.argv[2]
out_tree=sys.argv[3]

infile=open(metadatafile)
lines = infile.read()
infile.close()

infile=open(treefile)
tree = infile.read()
infile.close()

metadata={}
#lines=lines.replace(' ','_')
lines=lines.replace('(','')
lines=lines.replace(')','')
lines=lines.replace('"','')
lines=lines.split('\n') #split on return
lines=[line for line in lines if line.strip() !=""] #remove empty lines

for line in lines:
    metadata[line.split('\t')[0]]=line
for taxa in metadata:
    
    tree=tree.replace(taxa,(metadata[taxa].split('\t')[1]))

print(tree)

with open(out_tree, 'w') as newtree:
    newtree.write(tree)
    newtree.close()