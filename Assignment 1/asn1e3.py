# CIS*6060 Bioinformatics 
# Assignemnt 1 Question 3 
# Under the guidance of : Prof. Yan Yan
# Atharva Vichare
# Program : Master of Data Science
# 1320832


from Bio import SeqIO

#This functions summarizes the contents of a multi-FASTA file by displaying the header, first 10 amino acids, and the total number of amino acids for each sequence.
def summarize_fasta(fasta): 
    # Parse the FASTA file
    for record in SeqIO.parse(fasta, "fasta"):
        header = record.description
        sequence = str(record.seq)
        first_10 = sequence[:10]
        length = len(sequence)
        print(f">{header} {first_10} : {length}")

if __name__ == "__main__":
    fasta = input("Please input path of fasta file: ")
    summarize_fasta(fasta)
    print("Yayy you did it. Congrats :) :)")