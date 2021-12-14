import os
import sys
import glob
import operator

files = [fname for fname in glob.glob('*.fas')]

Alveolates = ['Gefiokel', 'Malacali', 'Malajako', 'Adunpalu', 'Ergocypr', 'Chilcaul', 'Chilcusp', 'Dysnbrev', 'Giardmuris', 'Giarlamb', 'Gyromonas', 'TrimitusIT1', 'Trimitussp', 'Hexamita004', 'TrepPPS6BOT', 'TrepPPS6MP', 'TrepoPC1', 'TrepPPS6DAR', 'TrepPPS6ERA', 'TrepPPS6Vla', 'TrepagMIS2C', 'TrepagPIG', 'TrepagSOOS', 'TrepstCONGO', 'Spirvort', 'Spirbark', 'Spirsalm', 'Kipfbial', 'Carpmemb', 'PAP20', 'PEICavEel', 'Retort01', 'RetortGEM', 'RetortLike', 'Monoexil', 'Parapyri', 'Trimmari', 'AfBUS', 'AfSCH', 'AiBMA', 'Dientafra', 'TrifoeBo', 'TrifoeFe', 'TrifoeGEN', 'TrifoePo', 'Trichbat', 'Pentahom', 'Tetragall', 'Trichgall', 'Trichtenax', 'Tricvagi']

d_genelen = {}
d_genemissing = {}
d_of_d = {}
taxa_list = []

def make_gene_dict(inf):
	infile = open(inf)
	line = infile.read()
	infile.close()
	seqs = line.split('>')[1:]
	gene_len = len(''.join(seqs[0].split('\n')[1:]))
	d_genelen[inf.split('.')[0]] = gene_len
	total = 0
	gaps = 0	
	d_header = {}
	for seq in seqs:
		header = seq.split()[0]
		if header.startswith('XP'):
			pass
		else:
			taxa_list.append(header)
		gene_seq = ''.join(seq.split('\n')[1:])
		if header in Alveolates:
			total = total + len(''.join(seq.split('\n')[1:]))
			gaps = gaps + gene_seq.count('-') + gene_seq.count('X')
		d_header[header] = gene_seq.count('-') + gene_seq.count('X')
        print(inf)
        print(total)
        try:
                d_genemissing[inf.split('.')[0]] = float(gaps)/float(total)
        except ZeroDivisionError:
                d_genemissing[inf.split('.')[0]] = float(100.0)
	return d_header


for fname in files:
	d_of_d[fname.split('.')[0]] = make_gene_dict(fname)

sorted_genes = sorted(d_genemissing.items(), key=operator.itemgetter(1), reverse=False)


out = open(sys.argv[1],'w')

taxa = set(taxa_list)

for taxon in taxa:
	out.write('\t%s' % (taxon))
out.write('\n')

c = 1


for gene in sorted_genes:
	out.write('%s' % (gene[0]))
	for taxon in taxa:
		full_len = 0
		num_gaps = 0
		for gene2 in sorted_genes[:c]:
			full_len = 	full_len + d_genelen[gene2[0]]
			try:
				num_gaps = num_gaps + d_of_d[gene2[0]][taxon]
			except KeyError:
				num_gaps = num_gaps + d_genelen[gene2[0]]
		
		final_number = (float(num_gaps)/float(full_len))
		out.write('\t%s' % (final_number))
	c = c + 1
	out.write('\n')
	
out.close()
