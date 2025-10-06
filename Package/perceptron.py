import numpy as np

class LogicError(Exception):
    def __init__(self, message="논리 값이 올바르지 않습니다"):
        super().__init__(message)




class Gate:

    def __init__(self,x1=0,x2=0):
        self.x1=x1
        self.x2=x2


    def AND_Gate(self,bias=-0.7):
        x = np.array([self.x1, self.x2])
        w = np.array([0.5, 0.5])
        self.b = bias
        tmp = np.sum(w*x) + self.b
        if tmp <= 0:
            if self.x1>0 or self.x2>0:
                raise LogicError()
            else: return 0
        else:
            if self.x1>0 and self.x2>0:
                return 1
            else: 
                raise LogicError()
        
        

    def OR_Gate(self,bias=-0.2):
        x = np.array([self.x1, self.x2])
        w = np.array([0.5, 0.5])
        self.b =bias
        tmp = np.sum(w*x) + self.b
        if tmp <= 0:
           return 0
        else:
           return 1    
    

    def NAND_Gate(self,bias=0.7):
        x = np.array([self.x1, self.x2])
        w = np.array([-0.5, -0.5])
        self.b = bias
        tmp = np.sum(w*x) + self.b
        if tmp <= 0:
            return 0
        else:
            return 1
        

    def NOR_Gate(self,bias=0.2):
        x = np.array([self.x1, self.x2])
        w = np.array([-0.5, -0.5])
        self.b =bias
        tmp = np.sum(w*x) + self.b
        if tmp <= 0:
           return 0
        else:
           return 1     


class Enhanced_Gate(Gate):
    def XOR(x1, x2):
        s1 = Gate.NAND_Gate(x1, x2)
        s2 = Gate.OR_Gate(x1, x2)
        y = Gate.AND_Gate(s1, s2)
        return y




if __name__ == '__main__':
   test1 = Gate(1,0)
   print(test1.AND_Gate())