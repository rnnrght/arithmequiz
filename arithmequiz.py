import random

class problem():
    """class for an arithmetic problem"""
    def __init__(self):
        self.a=random.randrange(0,10)
        self.b=random.randrange(0,10)
    def getoper(self):
        """ask the user for an operand"""
        self.op=raw_input("enter + or - ")
        if self.op=="+" or self.op=="-": return(self.op)
        else: self.getoper()
    def printproblem(self, oper):
        """print the problem"""
        if oper=="+":
            print("%d + %d" %(self.a, self.b))
            self.answer=self.a + self.b
        if oper=="-":
            print("%d - %d" %(self.a, self.b))
            self.answer=self.a - self.b
    def getanswer(self):
        """get answer from the user and check it"""
        self.ans=input(" = ")
        if self.ans==self.answer:
            print("correct!")
        else:
            print("wrong")

def cycle():
    """creates a problem object, prints the problem, and gets the answer"""
    prob=problem()
    prob.printproblem(prob.getoper())
    prob.getanswer()

#TODO: multiplication
#TODO: division (with remainders)
#TODO: ask multiple questions
#TODO: keep score
#TODO: keep score history
#TODO: have different player profiles

if __name__ == '__main__':
    cycle()


