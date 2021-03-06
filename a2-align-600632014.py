import sys,os

# Function definition is here
def gsa(Seq1,Seq2,Match,Mismatch,Gap): #Global Sequence Alignment
    row=[]
    for i in range(0,(len(Seq1)+1)):
        column = []
        for j in range(0,(len(Seq2)+1)):
            if(i == 0):
                if(j == 0):
                    column.append([j*Gap,[0,0,0]]) #[Value,[U,L,D]]
                else:
                    column.append([j*Gap,[0,1,0]]) #[Value,[U,L,D]]
            elif(j == 0):
                column.append([i*Gap,[1,0,0]]) #[Value,[U,L,D]]
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

def findSequencesAlignmentG(Source,Seq1,Seq2):
    Row = len(Seq1)
    Column = len(Seq2)
    sumDirect = []
    answerCount = 1
    while True:

        sumDirect = []
        ResultStr1 = []
        ResultStr2 = []  

        printLCSG(Source,Seq1,Seq2,Row,Column,ResultStr1,ResultStr2,sumDirect)
        print("Answer No. " + str(answerCount))
        print("Optimal Sequence 1 : "+''.join(ResultStr1))
        print("Optimal Sequence 2 : "+''.join(ResultStr2))
        print("------------------------------------")

        if (all(item == 1 for item in sumDirect)):
            break
        answerCount += 1
    return 0

def printLCSG(b,v,w,i,j,ResultStr1,ResultStr2,sumDirect):
    if (i == 0 or j == 0):
        if (b[i][j][1][2] == 1):
            ResultStr1.append(v[i-1])
            ResultStr2.append(w[j-1])
    
        return 0

    if (b[i][j][1][0] == 1):
        printLCSG(b,v,w,i-1,j,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append(v[i-1])
        ResultStr2.append("-")
        sumDirect.append(sum(b[i][j][1]))
        
        if ( sum(b[i][j][1]) !=1 ):
            b[i][j][1][0] = 0
    elif (b[i][j][1][1] == 1):
        printLCSG(b,v,w,i,j-1,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append("-")
        ResultStr2.append(w[j-1])
        sumDirect.append(sum(b[i][j][1]))
        
        if ( sum(b[i][j][1]) !=1 ):
            b[i][j][1][1] = 0

    else:          
        printLCSG(b,v,w,i-1,j-1,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append(v[i-1])
        ResultStr2.append(w[j-1])
        sumDirect.append(sum(b[i][j][1]))
    return 0

def findSequencesAlignmentL(Source,Seq1,Seq2):
    Row = len(Seq1)
    Column = len(Seq2)
    maxIndex = []
    maxVar = 0
    for i in range(0,(Row+1)):
        for j in range(0,(Column+1)):
            if ( maxVar < Source[i][j][0] ):
                maxVar = Source[i][j][0]

    for i in range(0,(Row+1)):
        for j in range(0,(Column+1)):
            if ( maxVar == Source[i][j][0] ):
                maxIndex.append([i,j])

    answerCount = 1
    for i in range(0,len(maxIndex)):
        sumDirect = []
        while True:

            sumDirect = []
            ResultStr1 = []
            ResultStr2 = []
            printLCSL(Source,Seq1,Seq2,maxIndex[i][0],maxIndex[i][1],ResultStr1,ResultStr2,sumDirect)
            print("Answer No. " + str(answerCount))
            print("Optimal Sequence 1 : "+''.join(ResultStr1))
            print("Optimal Sequence 2 : "+''.join(ResultStr2))
            print("------------------------------------")

            if (all(item == 1 for item in sumDirect)):
                break
        answerCount += 1

    return 0

def printLCSL(b,v,w,i,j,ResultStr1,ResultStr2,sumDirect):
    
    if (b[i][j][0] == 0):
        if (b[i][j][1][2] == 1):
            print(i,j,b[i][j][1],v[i-1])
            ResultStr1.append(v[i-1])
            ResultStr2.append(w[j-1])

        return 0

    if (b[i][j][1][0] == 1):
        printLCSL(b,v,w,i-1,j,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append(v[i-1])
        ResultStr2.append("-")
        sumDirect.append(sum(b[i][j][1]))
        
        if ( sum(b[i][j][1]) !=1 ):
            b[i][j][1][0] = 0

    elif (b[i][j][1][1] == 1):
        printLCSL(b,v,w,i,j-1,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append("-")
        ResultStr2.append(w[j-1])
        sumDirect.append(sum(b[i][j][1]))
        
        if ( sum(b[i][j][1]) !=1 ):
            b[i][j][1][1] = 0
    else:
        printLCSL(b,v,w,i-1,j-1,ResultStr1,ResultStr2,sumDirect)
        ResultStr1.append(v[i-1])
        ResultStr2.append(w[j-1])
        sumDirect.append(sum(b[i][j][1]))

    return 0

def displayResult(Source,Seq1,Seq2):
    Seq1 = "-"+(Seq1)
    Seq2 = "-"+(Seq2)
    Row = len(Seq1)
    Column = len(Seq2)
    Row1 = " "
    
    for j in range(0,Column):
        Row1 = Row1 + Seq2[j].rjust(4,' ')
    print(Row1)
    for i in range(0,Row):
        Result = Seq1[i]
        UpRow = " "
        for j in range(0,Column):
            if(Source[i][j][1][1] == 1):
                direct = "←"
            else:
                direct = " "
            Result = Result +direct+ str(Source[i][j][0]).rjust(3,' ')
            if (Source[i][j][1][2] == 1):
                diColumn = "↖"
            else:
                diColumn = " "
            if (Source[i][j][1][0] == 1):
                UpRow = UpRow + diColumn + "↑".rjust(3,' ')
            else:
                UpRow = UpRow + diColumn + " ".rjust(3,' ')
        print(UpRow)
        print(Result)      
    return 0
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
            displayResult(Result,Seq1,Seq2)
            print("====================================")
            findSequencesAlignmentG(Result,Seq1,Seq2)
        elif (sys.argv[6].upper() == 'L'):
            Result = lsa(Seq1,Seq2,Match,Mismatch,Gap)
            displayResult(Result,Seq1,Seq2)
            print("====================================")
            findSequencesAlignmentL(Result,Seq1,Seq2)
        else:
            print("error: Mode must be 'G' or 'L'\n")
            exit()  
    else:
        
        print("usage: python app.py [input sequence file1] [input sequence file2] [Match] [Mismatch] [Gap] [Mode].\nPlease, Try again.\n")

if __name__ == "__main__":
	main(sys.argv)
