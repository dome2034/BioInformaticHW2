import sys,os

# Function definition is here
def gsa(Seq1,Seq2,Match,Mismatch,Gap): #Global Sequence Alignment
    row=[]
    for i in range(0,(len(Seq1)+1)):
        column = []
        for j in range(0,(len(Seq2)+1)):
            if(i == 0):
                if(j == 0):
                    column.append([j*-1,[0,0,0]]) #[Value,[U,L,D]]
                else:
                    column.append([j*-1,[0,1,0]]) #[Value,[U,L,D]]
            elif(j == 0):
                column.append([i*-1,[1,0,0]]) #[Value,[U,L,D]]
            else:
                U = row[i-1][j][0]+Gap
                L = column[j-1][0]+Gap
                if(Seq1[i-1] == Seq2[j-1]):
                    D = row[i-1][j-1][0] + Match
                else:
                    D = row[i-1][j-1][0] + Mismatch
                Choose = max(U,L,D)
                if(Choose == U):
                    U = 1
                else:
                    U = 0
                if(Choose == L):
                    L = 1
                else:
                    L = 0
                if(Choose == D):
                    D = 1
                else:
                    D = 0
                column.append([Choose,[U,L,D]]) #[Value,[U,L,D]]
        row.append(column)
    return row

def lsa(Seq1,Seq2,Match,Mismatch,Gap): #Local Sequence Alignment
    row=[]
    for i in range(0,(len(Seq1)+1)):
        column = []
        for j in range(0,(len(Seq2)+1)):
            if(i == 0):
                column.append([0,[0,0,0]]) #[Value,[U,L,D]]
            elif(j == 0):
                column.append([0,[0,0,0]]) #[Value,[U,L,D]]
            else:
                U = row[i-1][j][0]+Gap
                L = column[j-1][0]+Gap
                if(Seq1[i-1] == Seq2[j-1]):
                    D = row[i-1][j-1][0] + Match
                else:
                    D = row[i-1][j-1][0] + Mismatch
                Choose = max(0,U,L,D)
                if(Choose == 0):
                    column.append([Choose,[0,0,0]]) #[Value,[U,L,D]]  
                else:
                    if(Choose == U):
                        U = 1
                    else:
                        U = 0
                    if(Choose == L):
                        L = 1
                    else:
                        L = 0
                    if(Choose == D):
                        D = 1
                    else:
                        D = 0
                    column.append([Choose,[U,L,D]]) #[Value,[U,L,D]]  
        row.append(column)
    return row
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
                for j in range(0,len(Seq2)+1):
                    print(Result[i][j])
                print("----------------")
        elif (sys.argv[6].upper() == 'L'):
            Result = lsa(Seq1,Seq2,Match,Mismatch,Gap)
            for i in range(0,len(Seq1)+1):
                for j in range(0,len(Seq2)+1):
                    print(Result[i][j])
                print("----------------")
        else:
            print("error: Mode must be 'G' or 'L'\n")
            exit()
    else:
        
        print("usage: python app.py [input sequence file1] [input sequence file2] [Match] [Mismatch] [Gap] [Mode].\nPlease, Try again.\n")

if __name__ == "__main__":
	main(sys.argv)
