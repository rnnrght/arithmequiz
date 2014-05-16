#!/usr/bin/python

import random
import csv
import time
import sys


#TODO: time limit
#TODO: add a default number of questions
#TODO: Make an option to the ask user for an operator
#TODO: make scorefile.csv a dotfile in user home dir


class NonIntegerError(Exception): pass 


class problem():
    """Class for an arithmetic problem."""

    def __init__(self):
        self.a=random.randrange(1,10)
        self.b=random.randrange(1,10)

    def getoper(self):
        """Pick a random operator"""
        return(random.choice(["+","-","*","/"]))

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
            createFile = raw_input("would you like me to create a scorefile?[y/n]  ")
            if createFile == "y" or "Y":
                self.scores = []
                self.hasscorefile = True
            else: #createFile == "n" or "N":
                print("OK.  Scores will not be recorded.")
                self.hasscorefile = False
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
        self.time=0.
        for score in self.scores:
            if score[0] == self.player:
                self.correct += int(score[1]) 
                self.total += int(score[2])
                self.time += float(score[3])
        return((self.correct, self.total, self.time))

    def printscoretally(self):
        self.scoretally = self.tallyscores()
        print("You have a total of %s correct out of %s in %s seconds." % self.scoretally)
        print("%s seconds per problem, %s seconds per correct answer" % (
        self.scoretally[0]/self.scoretally[2], self.scoretally[1]/self.scoretally[2]))


def cycle():
    """Creates a problem object, prints the problem, and gets the answer."""
    prob=problem()
    return(prob.getanswer())

def playgame():
    """Creates a problem set and cycles through it."""
    sc=scorecard()
    game=problemset()
    game.getnumberofproblems()
    starttime=time.time()
    game.playit()
    endtime=time.time()
    elapsedtime=endtime-starttime
    results = game.returnresults()
    print("\nYou got %s right out of %s in %s seconds." % (results[0], results[1], elapsedtime))
    if sc.hasscorefile: 
        results.append(elapsedtime)
        sc.addscore(results)
        sc.writescorefile(sc.scores)
        sc.printscoretally()

def gamemenu():
    print("""
1 Play game
2 View scores
3 Quit
    """)
    sel = raw_input("Enter your choice: ")
    if sel == "1":
        playgame()
        gamemenu()
    elif sel == "2":
        sc = scorecard()
        scoretally = sc.tallyscores()
        if scoretally != (0, 0, 0.0):
            sc.printscoretally()
            gamemenu()
        else:
            print("You seem to have an empty scorecard.  Play some games, won't you?")
            gamemenu()
    elif sel == "3":
        sys.exit()
    else: 
        gamemenu()

if __name__ == '__main__':
    gamemenu()
