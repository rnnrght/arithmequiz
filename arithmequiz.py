import random

class problem():
    """class for an arithmetic problem"""
    def __init__(self):
        self.a=random.randrange(1,10)
        self.b=random.randrange(1,10)
    def getoper(self):
        """pick a random operator"""
        return(random.choice(["+","-","*","/"]))
#TODO: Make this an option
#        """ask the user for an operand"""
#        self.op=raw_input("enter +, -, or * :")
#        if self.op=="+" or self.op=="-" or self.op=="*": return(self.op)
#        else: return(self.getoper())
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
        if oper=="/":
            self.denominator=self.a
            self.numerator=self.a * self.b
            print("%d / %d" %(self.numerator, self.denominator))
            self.answer=self.b
    def getanswer(self):
        """get answer from the user and check it"""
        self.ans=raw_input(" = ")
        try:
            if not self.ans.isdigit(): raise("NonIntegerInput")
        except: 
            print("please enter an integer")
            self.getanswer()
        if eval(self.ans)==self.answer:
            return(True)
        else:
            return(False)

class problemset():
    """represents a set of problems"""
    def __init__(self):
        self.problemnumbers=raw_input("How many problems would you like? ")
        try:
            if not self.ans.isdigit(): raise("NonIntegerInput")
        except:
            print("please enter an integer")
            self.problemnumbers=raw_input("How many problems would you like? ")
        self.score=0
    def playit(self):
        for i in range(eval(self.problemnumbers)): 
            self.res=cycle()
            if self.res: self.score +=1
    def printresults(self): 
        print("your score is %d right out of %d" %(self.score, eval(self.problemnumbers)))

def cycle():
    """creates a problem object, prints the problem, and gets the answer"""
    prob=problem()
    prob.printproblem(prob.getoper())
    return(prob.getanswer())

def playgame():
    """creates a problem set and cycles through it"""
    game=problemset()
    game.playit()
    game.printresults()

#TODO: keep score history
#TODO: have different player profiles

if __name__ == '__main__':
    playgame()
