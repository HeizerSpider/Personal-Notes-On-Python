#given a string of letters as input, count the number of each letter and store in a dictionary (ACGT), all capital letters only

def get_base_counts(string):
    dict={'A' : 0 , 'C':0 , 'G':0 , 'T':0}
    for i in string:
        if i=="A":
            dict['A']+=1
        elif i=="C":
            dict['C']+=1
        elif i=="G":
            dict['G']+=1
        elif i=="T":
            dict['T']+=1   
        else: 
            return False
    return dict         
        
if __name__=="__main__":
    print(get_base_counts('TTTTAGGCB'))
    print(get_base_counts('TTAAGGCC'))