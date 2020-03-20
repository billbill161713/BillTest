import random,numpy as np

class Array:
    def __init__(self, arrayone, arraysize1, arraysize2, number1, number2):
        self.arrayone = arrayone
        self.arraysize1 = arraysize1
        self.arraysize2 = arraysize2
        self.number1 = number1
        self.number2 = number2
        
        
        
        
        
    def comparelastnumber(self):
        y = list(range(1, self.arraysize1 * self.arraysize2 + 1))
        #生成1~25數字(位置)
        random.shuffle( y)
        #洗牌
        z=[]
        #籤筒
        for j in range( 0, self.arraysize2 * self.arraysize1):
            z.append( self.randomtest( self.number1, self.number2))
            random.shuffle( z)
            #塞25個隨機數字進去


        for i in range( 0 , self.arraysize1 * self.arraysize2):
            self.arrayone[ self.testinterval( y[i], self.arraysize2) - 1][ self.testlen( y[i], self.arraysize2) - 1] = z[i]
            #Y抽隨機位置，Interval與Len是分排列
        self.lastNumber()
        #判斷最後數字
        return  self.compare_fb(self.arrayone)
    def lastNumber(self):
        if self.arrayone[ self.arraysize1 - 1][ self.arraysize2 - 1] == self.arrayone[ self.arraysize1 - 1]\
        [ self.arraysize2 - 2] or self.arrayone[ self.arraysize1 - 1][ self.arraysize2 - 1] == \
        self.arrayone[ self.arraysize1 - 2][ self.arraysize2 - 1]:
            self.comparelastnumber()
            
            
    #比相同，如果相同會給他新數字
    def samejudgment(self,frontnumber,behindbumber):#Compare
        z=2
        for i in range(0,z):
            if frontnumber == behindbumber:
                behindbumber=self.randomtest(self.number1,self.number2)
            else:
                break
            z=z+1
        return behindbumber
    
    #判斷上下左右,使用SameJudgment判斷並給予新數字
    def compare_fb( self, x):#Front and back and up and down
        for i in range( 0, self.arraysize1):
            for j in range( 0, self.arraysize2):
                if i < self.arraysize1-1:
                    x[ i + 1 ][ j ]=int( self.samejudgment( x[ i ][ j ],x[ i + 1][ j ]))
                if j < self.arraysize2 - 1:
                    x[ i ][ j + 1 ]=int( self.samejudgment(x[ i ][ j ],x[ i ][ j + 1 ]))
        return x
                    
        


    def randomtest( self, number1, number2):#生成隨機數
        return random.randint( number1, number2)


    def testinterval( self, numbertest, array2):
        return int( numbertest / array2)


    def testlen( self, numbertest, array2):
        return int( numbertest % array2)
    
    
    def maxnumber( self, x):
        number=self.number1
        for i in range(0,self.arraysize1):
            for j in range(0,self.arraysize2):
                if number<x[i][j]:
                    number=x[i][j]
        return number
    
    
    def meannumber( self, x):
        number=0
        for i in range(0,self.arraysize1):
            for j in range(0,self.arraysize2):
                number=x[i][j]+number
        number=number/(self.arraysize1*self.arraysize2)
        return number
    
    
    def testrun(self,runnumber):
        for i in range(0,runnumber):
            print("測試數",i+1)
            print(self.comparelastnumber())
            






