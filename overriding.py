#Overridng
class Parent:
	# can use anything in place of self
	def myMethod(self):
		print("Parent Class")

class Child(Parent):
	def myMethod(self):
		print("Child Class")

obj = Child()
obj.myMethod()