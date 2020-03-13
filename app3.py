import util.util13 as util
import numpy as np

if __name__ == '__main__':
    global Number1,Number2,Array1,Array2
    Number1=11
    Number2=30
    Array1=5
    Array2=5
    arrayone=np.zeros([Array1,Array2], dtype = int)
    input=util.CompareLastnumber(arrayone,Array1,Array2,Number1,Number2)
    input=util.CompareFB(input,Array1,Array2)
    print(input)
    util.Unique(input)
    print("")
    util.MaxNumber(input)
    print("")
    util.MeanNumber(input)
    print("")
    util.TestRun(10,input,Array1,Array2,Number1,Number2)