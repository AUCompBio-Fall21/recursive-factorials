#! /usr/bin/python3

from Bio import SeqIO
import re

# To read the fasta file

#f = open('Aubie.fasta', 'r')
#lines = f.readlines()

def__init__(self, sample, date):
    for seq_record in SeqIO.parse("Aubie.fasta", "fasta"):
	str = seq_rec.id
	print(str)
	self.sample = print(str.split('_')[0])
	self.date = print(str.split('_')[1])

