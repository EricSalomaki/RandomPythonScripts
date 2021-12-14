import sys
import os

logfile = sys.argv[1]

infile = open(logfile)
lines = infile.read()
infile.close()

lines=lines.split('\n')
lines=[line for line in lines if line.strip() !=""] #remove empty lines
lastline = lines[-1]

gene=(logfile.split("_new"))

if "Date" not in lastline:   
    print(gene[0]+ " tree unfinished")
else:
    pass