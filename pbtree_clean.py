import sys
import os

dirty=sys.argv[1]

infile=open(dirty)
lines=infile.readlines()
infile.close

cleantrees = []
for line in lines:
	openbracket=line.count("(")
	closebracket=line.count(")")
	if openbracket == closebracket:
		cleantrees.append(line)
print(cleantrees)	

cleaned=open(sys.argv[2], "w")
for tree in cleantrees:
	cleaned.write(tree)
cleaned.close()
