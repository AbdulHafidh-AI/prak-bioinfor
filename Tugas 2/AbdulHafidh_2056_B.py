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


argumentInput = args['input']
argumentOutput = args['output'] + ".xml"

id_ncbi = argumentInput





Entrez.email = "hafidhabdul4444@gmail.com"



with Entrez.efetch(db= "nucleotide", rettype= "gb", retmode= "fasta", id=id_ncbi) as handle:
    for record in SeqIO.parse(handle, 'gb'):
        print(record.id)
        print(record.description)
        print(record.seq)
         # write to fasta file
        with open(record.id + str(".fasta"), 'w') as f:
            f.write('>' + record.description + '\n')
            # new line every 80 characters
            for i in range(0, len(record.seq), 80):
                f.write(str(record.seq[i:i+80]) + '\n')
            f.close()

blast_result = NCBIWWW.qblast('blastn', 'nt',id_ncbi)

with open(argumentOutput, 'w+') as save_to:
    save_to.write(blast_result.read())
    blast_result.close()

result_handle = open(argumentOutput, 'r')
blast_record = NCBIXML.read(result_handle)

E_VALUE_TRESHOLD = 0.0001
ct = 0

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        ct = ct +1
        if hsp.expect < E_VALUE_TRESHOLD:
            print('\n')
            print('*** alignment ***')
            print('Sequence : ', alignment.title)
            print('Lenght : ', alignment.length)
            print('E Value : ', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')



# run with : python AbdulHafidh_2056_B.py -i (id_ncbi) -o (nama_file_output dalam format xml)
# example : python AbdulHafidh_2056_B.py -i NC_000913.3 -o blast_isolate
# tidak perlu lagi menambahkan ekstensi .xml pada nama file output karena sudah otomatis ditambahkan


