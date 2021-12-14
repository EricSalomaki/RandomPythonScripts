import sys
import pandas as pd


def get_best_hit (blast_out):


	data = pd.read_csv(blast_out, sep = "\t", names = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'])
	df = pd.DataFrame(data)
	list_of_names = []

	for row_index, row in df.iterrows():

		sseqid = row['sseqid']
		evalue = row['evalue']
		pident = row['pident']
		qseqid = row['qseqid']
		qseqid = qseqid.split('+')[0]

		if evalue == 0.0  or pident >= 99.0 and sseqid not in list_of_names:
			print(sseqid)
			list_of_names.append(qseqid + '+' + sseqid + '\t' + sseqid)
		else:
			pass

	return list_of_names


def main():

	blast_out = open(sys.argv[1])
	results = get_best_hit(blast_out)

	with open(sys.argv[2], 'w') as outfile:
		for element in results:
			outfile.write(element + "\n")


if __name__ == '__main__':
		main()