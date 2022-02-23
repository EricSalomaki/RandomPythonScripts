import sys
import os
from Bio import SeqIO

# get masterDB path
metadata = open(sys.argv[1])
md = metadata.read()
metadata.close()

md = md.split('\n')
md = [m for m in md if m.strip() !='']
taxa_d = {}

for m in md:
	taxa_d[m.split('\t')[0]] = m.split('\t')
	
fasta = SeqIO.parse(open(sys.argv[2]), 'fasta')
rename = []
name_d = {}
new_d = {}	
for record in fasta:
	r = record.id
	rname_w_space = record.id 
	recname = record.id
	pnum = record.id
	if '..' in r:
		recname = r.split('..')[0] 
		pnum = r.split('..')[1]
		rname_w_space = recname.replace('_', ' ')
	else:
		rname_w_space = r.replace('_', ' ')

	for k,v in taxa_d.items():
		fullname = v[1].strip('.')
		if fullname == rname_w_space:
			name_d[r] = k + '..' + pnum
		else:
			pass
	if r not in name_d:
		new_d[r] = record
	else:
		for k,v in name_d.items():
			if k == r:
				record.id = v
				record.description = v
				new_d[r] = record
			else:
				pass
			
with open(sys.argv[3], "w") as renamed:
	SeqIO.write(new_d.values(), renamed, "fasta")
		

