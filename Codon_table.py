# Generate codon table as a python dictionary 
# from http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/ 

bases = "tcag"
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

# Get all the Marchantia chloroplast CDS

with open("/Users/annatswater/Desktop/Marchantia_cds_test.txt", "r+") as f:
    Name = [] # open an empty list for names of genes 
    for line in f:
        nextLine = next(f)
        codon = ""
        for letters in nextLine:
            if len(codon) == 3:

                
                
            elif len (codon) < 3: 
                codon += letter

            else:
                break # if > 3 quit loop 
            
            
        if line.startswith(">") == True: 
            line = line.rstrip()
            Name.append(line)
            
    # print(Name[0]) will return the first item, thus can use index to match things
    
            



