import sys

########################################
#
# Usage: python cut_sequence.py fastafile sequencelength
# Example: python cut_sequence.py test_seq.fa 100
# Outputfile: newfastafile
#
########################################

def cut_sequence(fasta_file, length):
    f= open(fasta_file,"r")
    #print(f)
    newfile = open("newfastafile", "w+")
    sequence= ''
    fastaheader = ''
    seq_cut = ''
    for fasta_seq in f.readlines():
        print(fasta_seq)
        if fasta_seq.strip()[0]=='>':
            fastaheader= fasta_seq.strip()
            #print('fastaheader= ',fastaheader)
        else:
            sequence =sequence+ str(fasta_seq.replace("\n", ""))
            #print('sequence= ',sequence)
    seq_cut= sequence[0:length]

    newfile.write(fastaheader+"\n")
    newfile.write(seq_cut)

userParameters = sys.argv[1:]

try:
    if len(userParameters) == 1:
        cut_sequence(userParameters[0])
    elif len(userParameters) == 2:
        cut_sequence(userParameters[0], int(userParameters[1]))
    else:
        print("There is a problem!!")
except:
    print("There is a problem!")