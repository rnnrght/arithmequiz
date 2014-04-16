import random

class problem():
    """class for an arithmetic problem"""
    def __init__(self):
        self.a=random.randrange(0,10)
        self.b=random.randrange(0,10)
    def getoper(self):
        """ask the user for an operand"""
        self.op=raw_input("enter +, -, or * :")
        if self.op=="+" or self.op=="-" or self.op=="*": return(self.op)
        else: self.getoper()
    def printproblem(self, oper):
        """print the problem"""
        if oper=="+":
            print("%d + %d" %(self.a, self.b))
            self.answer=self.a + self.b
        if oper=="-":
            print("%d - %d" %(self.a, self.b))
            self.answer=self.a - self.b
        if oper=="*":
            print("%d * %d" %(self.a, self.b))
            self.answer=self.a * self.b
    def getanswer(self):
        """get answer from the user and check it"""
        self.ans=input(" = ")
        if self.ans==self.answer:
            return(True)
        else:
            return(False)

class problemset():
    """represents a set of problems"""
    def __init__(self):
        self.problemnumbers=input("How many problems would you like? ")
        self.score=0
    def doit(self):
        for i in range(self.problemnumbers): 
            self.res=cycle()
            if self.res: self.score +=1
    def results(self): print("your score is %d right out of %d" %(self.score, self.problemnumbers))

def cycle():
    """creates a problem object, prints the problem, and gets the answer"""
    prob=problem()
    prob.printproblem(prob.getoper())
    return(prob.getanswer())

def playgame():
    """creates a problem set and cycles through it"""
    game=problemset()
    game.doit()
    game.results()

#TODO: division (with remainders)
#TODO: keep score history
#TODO: have different player profiles

if __name__ == '__main__':
    playgame()
