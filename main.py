# def mul(a):
# 	return lambda b:b*a

# singler = mul(1)    # addition = lambda b:b*1
# doubler = mul(2)    # addition = lambda b:b*2
# tripler = mul(3)    # addition = lambda b:b*3

# print(doubler(7))  #  7*2 = 14
# print(tripler(7))  #  7*3 = 21
# print(singler(7))  #  7*1 = 7

class Student:
	def __init__(self, fname):
		self.fname = fname
	def greet(self, fname):
		return f"Hello, {fname}"

class BatchA(Student):
	def __init__(self, lname):
		self.lname = lname
		#Student.__init__(self, "Nikunj")
		super().__init__("Nikunj")
	def printName(self):
		return f"{self.fname} {self.lname}"


stud = BatchA("Thakor")
print(stud.printName())










rgb(255, 255, 255)    # White
rgb(255, 0, 0)    # Red
rgb(0, 0, 0)    # Black
rgb(0, 255, 255)    # Cyan
rgb(255, 255, 0)    # Yellow


#00ff00   //green
#1e90ff   //dodgerblue

