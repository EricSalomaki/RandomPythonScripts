import sys
from Bio import SeqIO
import shutil


fas = sys.argv[1]
infasta = SeqIO.parse(fas, "fasta")

newdir = sys.argv[2]

crypto = []
for record in infasta:
	print(record)
	if "Cryptosporidium_proliferans" in record.id:
		crypto.append("FOUND")
	else:
		pass
if "FOUND" not in crypto:
	gene = fas.split("_new")[0]
	shutil.move(fas, newdir)
	shutil.move(gene + ".tre", newdir)
else:
	pass
	

