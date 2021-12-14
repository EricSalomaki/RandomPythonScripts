import dendropy
import sys

newick=sys.argv[1]
nexus=sys.argv[2]

mle = dendropy.Tree.get(path=newick, schema="newick")
mle.write(path=nexus, schema="nexus")
