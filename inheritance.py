# Single inheritance
class Parent:
    parentname = ""
    childname = ""
 
    def show_parent(self):
        print(self.parentname)
    def fun(self):
    	print("In class Base 1")
 
 
# Child class created inherits Parent class
class Child(Parent):
    def show_child(self):
        print(self.childname)
 
 
ch1 = Child()  # Object of Child class
ch1.parentname = "Mark"   # Access Parent class attributes
ch1.childname = "John"
ch1.show_parent()   # Access Parent class method
ch1.fun()
ch1.show_child()    # Access Child class method

#Multiple inheritance
class First:
	def __init__(self):
		# super(First,self).__init__()
		print("first")
class Second:
	def __init__(self):
		super(Second,self).__init__()
		print("second")
class Third(Second,First):
	def __init__(self):
		super(Third,self).__init__()
		print("Third")

Third()

# Multilevel inheritance
class Animal:
	def base (self):
		print("Base Animal Class")
class Dog(Animal):
	def bark(self):
		print("Barking...")
class Baby_Dog(Dog):
	def weep (self):
		print("Weeping...")
d = Baby_Dog()
d.base()
d.bark()
d.weep()




