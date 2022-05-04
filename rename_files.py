import sys
import os
import glob

#Rename files based on tab-separated list of old \t new names

infile = open(sys.argv[1], 'r')
lines=infile.read()

lines=lines.split('\n') #split on return
lines=[line for line in lines if line.strip() !=""] #remove empty lines

filepath = sys.argv[2]
tsvfiles = (glob.glob(filepath +"/*.tsv"))

name_d = {}
for line in lines:
	name_d[line.split('\t')[0]] = line

	
for file in tsvfiles:
	file = file.split('/')[-1]
	file = file.split('.tsv')[0]
	for k,v in name_d.items():
		if file == k:
			new = v.split('\t')[1]
			print(new)
			os.rename(file + '.tsv', new + '.tsv')
