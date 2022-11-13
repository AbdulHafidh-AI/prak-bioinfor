import argparse
from Bio import SeqIO
from Bio import Entrez
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# Membuat objek parser
arg = argparse.ArgumentParser()

# Menambahkan argumen untuk melakukan proses command line argument
arg.add_argument("-i", "--input", help="Input file",type=str)
arg.add_argument("-o", "--output", help="Output file .", type=str, default="")

# parsing argumen
args = vars(arg.parse_args())


argumentInput = args['input'] # halo
argumentOutput = args['output'] + ".xml" # tes.xml


print(argumentInput)
print(argumentOutput)