import sys


name_file=open(sys.argv[1])# TSV of names to be changed (old name tab new name)
lines=name_file.read()
name_file.close()

stripped_lines = [l.rstrip() for l in lines]

name_dict={}
for item in stripped_lines:
    key, value = item.split('\t')
    name_dict[key]=(value)
    
  
treefile=open(sys.argv[2]) #tree file to rename
tree = treefile.read()


for k, v in name_dict.items(): #search in the tree for k     
    tree = tree.replace(k,v)

renamed_tree=open(sys.argv[2] + '.renamed.tre', 'w')
renamed_tree.write(tree)
renamed_tree.close()
