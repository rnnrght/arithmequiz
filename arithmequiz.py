import random

class problem():
	def __init__(self):
		self.a=random.randrange(0,10)
		self.b=random.randrange(0,10)
	def printproblem(self, oper):
		if oper=="addition":
			print("%d + %d" %(self.a, self.b))
			self.answer=self.a + self.b
		if oper=="subtraction":
			print("%d - %d" %(self.a, self.b))
			self.answer=self.a - self.b
	def getanswer(self):
		self.ans=input(" = ")
		if self.ans==self.answer:
			print("correct!")
		else:
			print("wrong")

def cycle():
	prob=problem()
	prob.printproblem("addition")
	prob.getanswer()


