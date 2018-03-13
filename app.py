import sys,os

# Function definition is here
def gsa(Seq1,Seq2,Match,Mismatch,Gap): #Global Sequence Alignment
    Score=[]
    for i in range(0,(len(Seq1)+1)):
        column = []
        for j in range(0,(len(Seq2)+1)):
            if(i == 0):
                column.append(j*-1)
            elif(j == 0):
                column.append(i*-1)
            else:
                U = Score[i-1][j]+Gap
                L = column[j-1]+Gap
                if(Seq1[i-1] == Seq2[j-1]):
                    UL = Score[i-1][j-1] + Match
                else:
                    UL = Score[i-1][j-1] + Mismatch
                Choose = max(U,L,UL)
                column.append(Choose)
        Score.append(column)
    return Score

def lsa(Seq1,Seq2,Match,Mismatch,Gap): #Local Sequence Alignment
    Score=[]
    for i in range(0,(len(Seq1)+1)):
        column = []
        for j in range(0,(len(Seq2)+1)):
            if(i == 0):
                column.append(0)
            elif(j == 0):
                column.append(0)
            else:
                U = Score[i-1][j]+Gap
                L = column[j-1]+Gap
                if(Seq1[i-1] == Seq2[j-1]):
                    UL = Score[i-1][j-1] + Match
                else:
                    UL = Score[i-1][j-1] + Mismatch
                Choose = max(0,U,L,UL)
                column.append(Choose)
        Score.append(column)
    return Score
#============================= 
    
    
def main(argv):
    
    Seq1 = ''
    Seq2 = ''

    if (len(sys.argv) == 7):
        FileName1 = sys.argv[1]
        if (os.path.exists('./' + FileName1)):
            fo = open(str(FileName1))    
            for row in fo:
                Seq1 += row.replace('\n','')
            fo.close()
        else:
            print("error: file 1",FileName1,"not found!\n")
            exit()
        
        FileName2 = sys.argv[2]
        if (os.path.exists('./' + FileName2)):
            fo = open(str(FileName2))       
            for row in fo:
                Seq2 += row.replace('\n','')
            fo.close()
        else:
            print("error: file 2",FileName2,"not found!\n")
            exit()
            
        try:
            Match = int(sys.argv[3])
        except ValueError:
            print("error: Match must be numeric\n")
            exit()
            
        try:
            Mismatch = int(sys.argv[4])
        except ValueError:
            print("error: Mismatch must be numeric\n")
            exit()
            
        try:
            Gap = int(sys.argv[5])
        except ValueError:
            print("error: Gap must be numeric\n")
            exit()
            
        if (sys.argv[6].upper() == 'G'):
            Result = gsa(Seq1,Seq2,Match,Mismatch,Gap)
            for i in range(0,len(Seq1)+1):
                print(Result[i])
        elif (sys.argv[6].upper() == 'L'):
            Result = lsa(Seq1,Seq2,Match,Mismatch,Gap)
            for i in range(0,len(Seq1)+1):
                print(Result[i])
        else:
            print("error: Mode must be 'G' or 'L'\n")
            exit()
    else:
        
        print("usage: python app.py [input sequence file1] [input sequence file2] [Match] [Mismatch] [Gap] [Mode].\nPlease, Try again.\n")

if __name__ == "__main__":
	main(sys.argv)
