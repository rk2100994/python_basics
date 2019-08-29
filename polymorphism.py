class Animal:
	def __init__(self):
		print("I'm in animal")

class Dog(Animal):
	def talk(self):
		print("I talk in barking fashion")

class Lion(Animal):
	def talk(self):
		print("I talk in roaring way")

an1 = Lion()
an2 = Dog()
an1.talk()
an2.talk()
