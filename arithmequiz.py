import random
import csv

class NonIntegerError(Exception): pass 

class problem():
    """Class for an arithmetic problem."""

    def __init__(self):
        self.a=random.randrange(1,10)
        self.b=random.randrange(1,10)

    def getoper(self):
        """Pick a random operator"""
        return(random.choice(["+","-","*","/"]))
#TODO: Make this an option
#        """ask the user for an operator"""
#        self.op=raw_input("enter +, -, or * :")
#        if self.op=="+" or self.op=="-" or self.op=="*": return(self.op)
#        else: return(self.getoper())

    def construcproblem(self, oper):
        """Construct the string representation of the problem and
        calculate the answer.
        """
        if oper=="+":
            self.answer=self.a + self.b
            return("%d + %d" %(self.a, self.b))
        if oper=="-":
            self.answer=self.a - self.b
            return("%d - %d" %(self.a, self.b))
        if oper=="*":
            self.answer=self.a * self.b
            return("%d * %d" %(self.a, self.b))
        if oper=="/":
            self.answer=self.b
            self.denominator=self.a
            self.numerator=self.a * self.b
            return("%d / %d" %(self.numerator, self.denominator))

    def getanswer(self):
        """Print problem, get answer from the user, and check it."""
        self.ans=raw_input(self.construcproblem(self.getoper()) + " = ")
        try:
            if not self.ans.replace("-","").isdigit(): 
                raise NonIntegerError 
        except NonIntegerError: 
            print("Please enter an integer")
            self.getanswer()
        if eval(self.ans)==self.answer:
            return(True)
        else:
            return(False)

class problemset():
    """Represents a set of problems."""

    def __init__(self):
        self.score = 0

    def getnumberofproblems(self):
        self.problemnumbers=raw_input("How many problems would you like? ")
        try:
            if not self.problemnumbers.isdigit(): 
                raise NonIntegerError 
        except NonIntegerError:
            print("Please enter an integer.")
            self.getnumberofproblems()

    def playit(self):
        for i in range(eval(self.problemnumbers)): 
            self.res=cycle()
            if self.res: self.score +=1

    def returnresults(self):
        return([self.score, eval(self.problemnumbers)])
        
class scorecard():
    """Keeps track of scores of multiple players."""

    def __init__(self):
        try:
            self.scores = csv.reader(open("scorecard.csv","r"))
            self.scores = [l for l in self.scores]
            self.hasscorefile=True
        except:
            self.hasscorefile=False
            print("No scorefile present, someday I'll ask you to create one.")
        self.player = raw_input("What is your player name? ")

    def addscore(self, score):
        score.insert(0, self.player)
        self.scores.append(score)

    def writescorefile(self,s):
        with open('scorecard.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(s)

    def tallyscores(self):
        self.correct=0
        self.total=0
        for score in self.scores:
            if score[0] == self.player:
                self.correct += int(score[1]) 
                self.total += int(score[2])
        return((self.correct,self.total))

def cycle():
    """Creates a problem object, prints the problem, and gets the answer."""
    prob=problem()
    return(prob.getanswer())

def playgame():
    """Creates a problem set and cycles through it."""
    sc=scorecard()
    game=problemset()
    game.getnumberofproblems()
    game.playit()
    results = game.returnresults()
    print("You got %s right out of %s." % (results[0], results[1]))
    if sc.hasscorefile: 
        sc.addscore(game.returnresults())
        sc.writescorefile(sc.scores)
        print("You have a total of %s correct out of %s" % sc.tallyscores())

#TODO: add a timer / time limit
#TODO: add a default number of questions

if __name__ == '__main__':
    playgame()
