import random,numpy as np
global Number1,Number2,Array1,Array2
Number1=10
Number2=20
Array1=5
Array2=5
def CompareLastnumber():
    x=np.random.randint(Number1,Number2,[Array1,Array2])
    z=2
    for i in range(0,z):
        if x[Array1-1][Array2-2]==x[Array1-1][Array1-1]:
            np.random.randint(Number1,Number2,[Array1,Array2])
        else:
            break
        z=z+1
    return x
def SameJudgment(FrontNumber,BehindNumber):#Compare
    z=2
    for i in range(0,z):
        if BehindNumber == FrontNumber:
            FrontNumber=Random()
        else:
            break
        z=z+1
    return FrontNumber
def CompareFB(x):#Front and back
    for i in range(0,Array1):
        for j in range(0,Array2-1):
            x[i][j]=SameJudgment(x[i][j],x[i][j+1])
    return x

def CompareUD(x):# up and down
    for i in range(0,Array1-1):
        for j in range(0,Array2):
            x[i][j]=SameJudgment(x[i][j],x[i+1][j])
    return x 
def Random():
    return random.randint(Number1,Number2)
    