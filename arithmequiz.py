import random
import csv

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
            if not self.problemnumbers.isdigit(): raise("NonIntegerInput")
        except:
            print("please enter an integer")
            self.problemnumbers=raw_input("How many problems would you like? ")
        self.score=0
    def playit(self):
        for i in range(eval(self.problemnumbers)): 
            self.res=cycle()
            if self.res: self.score +=1
    def returnresults(self):
        return([self.score, eval(self.problemnumbers)])
        
class scorecard():
    """scorecard keeps track of scores of multiple players"""

    def __init__(self):
        try:
            self.scores = csv.reader(open("scorecard.csv","r"))
            self.scores = [l for l in self.scores]
            self.hasscorefile=True
        except:
            self.hasscorefile=False
            print("no scorefile present, someday I'll ask you to create one")
        self.player = raw_input("what is your player name? ")

    def addscore(self, score):
        score.insert(0, self.player)
        self.scores.append(score)

    def writescorefile(self,s):
        with open('scorecard.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(s)

def cycle():
    """creates a problem object, prints the problem, and gets the answer"""
    prob=problem()
    prob.printproblem(prob.getoper())
    return(prob.getanswer())

def playgame():
    """creates a problem set and cycles through it"""
    sc=scorecard()
    game=problemset()
    game.playit()
    results = game.returnresults()
    print("you got %s right out of %s" % (results[0], results[1]))
    sc.addscore(game.returnresults())
    if sc.hasscorefile: sc.writescorefile(sc.scores)

#TODO: have different player profiles
#TODO: add a timer / time limit
#TODO: add a default number of questions

if __name__ == '__main__':
    playgame()
