import os
import sys
import glob



def process_files(treefile, outfile):
	infile = open(treefile)
	line = infile.read()
	infile.close()
	try:
		crap = line.split('TAXLABELS')[1]
		out = open(outfile, 'w')
		startshit = line.split('TAXLABELS')[0]
		out.write(startshit)
		out.write('TAXLABELS\n')
		taxashit = line.split('TAXLABELS')[1]
		taxa = taxashit.split(';\nEND;')[0]
		endfile = taxashit.split(';\nEND;')[1]
		for taxon in taxa.split('\n'):
			if taxon.strip() in to_color:
				out.write('\t%s[&!color=#d92124]\n' % (taxon))
			else:
				out.write('\t%s\n' % (taxon))
		out.write(';\nEND;')
		out.write(endfile)
		out.close()
	except IndexError:
		crap = line.split('taxlabels')[1]
		out = open(outfile, 'w')
		startshit = line.split('taxlabels')[0]
		out.write(startshit)
		out.write('taxlabels\n')
		taxashit = line.split('taxlabels')[1]
		taxa = taxashit.split(';\nend;')[0]
		endfile = taxashit.split(';\nend;')[1]
		for taxon in taxa.split('\n'):
			if taxon.strip() in to_color:
				out.write('\t%s[&!color=#d92124]\n' % (taxon))
			else:
				out.write('\t%s\n' % (taxon))
		out.write(';\nend;')
		out.write(endfile)
		out.close()		
	
files = [fname for fname in glob.glob('*.nex')]
infile = open('GoodApiHomologs.list')
lines = infile.readlines()
infile.close()
to_color = []
for i in lines:
	to_color.append(i.strip())
print(to_color)

for fname in files:
	print(fname)
	process_files(fname, '%s_colored.tre' % (fname))