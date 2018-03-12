import sys,os

# Function definition is here


#============================= 
    
    
def main(argv):
    
    Seq1=[]
    Seq2=[]
    Match = 0
    Mismatch = 0
    Gap = 0
    Mode = 'G'
    
    if (len(sys.argv) == 6):
        FileName1 = sys.argv[1]
        if (os.path.exists('./' + FileName1)):
            fo = open(str(FileName1))    
            for row in fo:
                if (row[0] != '>'):
                    Seq1.append(row.replace('\n',''))
            fo.close()
        else:
            print("error: file 1",FileName1,"not found!\n")
            exit()
        
        FileName2 = sys.argv[2]
        if (os.path.exists('./' + FileName2)):
            fo = open(str(FileName2))       
            for row in fo:
                if (row[0] != '>'):
                    Seq2.append(row.replace('\n',''))
            fo.close()
        else:
            print("error: file 2",FileName2,"not found!\n")
            exit()
            
        if (sys.argv[3].isnumeric()):
            Match = sys.argv[3]
        else:
            print("error: Match must be numeric\n")
            exit()
        
        if (sys.argv[4].isnumeric()):
            Mismatch = sys.argv[4]
        else:
            print("error: Match must be numeric\n")
            exit()
            
        if (sys.argv[5].isnumeric()):
            Gap = sys.argv[5]
        else:
            print("error: Match must be numeric\n")
            exit()
            
        if (sys.argv[6].upper() == 'G'):
            print("G\n")
        elif (sys.argv[6].upper() == 'L'):
            print("L\n")
        else:
            print("error: Mode must be 'G' or 'L'\n")
            exit()
    else:
        
        print("usage: python app.py [input sequence file1] [input sequence file2] [Match] [Mismatch] [Gap] [Mode].\nPlease, Try again.\n")

if __name__ == "__main__":
	main(sys.argv)
