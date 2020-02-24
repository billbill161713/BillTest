import random,numpy as np


global Number1,Number2,Array1,Array2
Number1=11
Number2=30
Array1=5
Array2=5


def CompareLastnumber():
    x=np.zeros([Array1,Array2], dtype = int)
    #print(x)
    y=list(range(1,Array1*Array2+1))#Draw position
    random.shuffle(y)
    z=[]#Draw number
    for j in range(0,Array2*Array1):
        z.append(Random(Number1,Number2))


    for i in range(0,Array1*Array2):
        x[TestInterval(y[i])-1][TestLen(y[i])-1]=z[i]
    LastNumber(x)
    return x


def LastNumber(x):
    if x[Array1-1][Array2-1]==x[Array1-1][Array2-2] or x[Array1-1][Array2-1]==x[Array1-2][Array2-1]:
        CompareLastnumber()


def TestInterval(NumberTest):
    return int(NumberTest/Array2)


def TestLen(NumberTest):
    return int(NumberTest%Array2)
    
    
def SameJudgment(FrontNumber,BehindNumber):#Compare
    z=2
    for i in range(0,z):
        if FrontNumber == BehindNumber:
            BehindNumber=Random(Number1,Number2)
        else:
            break
        z=z+1
    return BehindNumber


def CompareFB(x):#Front and back and up and down
    for i in range(0,Array1):
        for j in range(0,Array2):
            if i<Array1-1:
                x[i+1][j]=SameJudgment(x[i][j],x[i+1][j])
            if j<Array2-1:
                x[i][j+1]=SameJudgment(x[i][j],x[i][j+1])
    return x


def Random(Number1,Number2):
    return random.randint(Number1,Number2)
    

def Unique(x):
    u = np.unique(x)
    u,indices = np.unique(x, return_index = True)
    u,indices = np.unique(x,return_counts = True)
    for i in range(0,len(u)):
        print("DuplicateNumbers:"+str(u[i]))
        print("RepeatNumber:"+str(indices[i]))
def MaxNumber(x):
    print("MaxNumber:"+str(np.amax(x)))
def MeanNumber(x):
    print("MeanNumber:"+str(np.mean(x)))
def TestRun(RunNumber):
    for i in range(0,RunNumber):
        input=CompareLastnumber()
        input=CompareFB(input)
        print(input)