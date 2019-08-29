# class Car:
# 	def __init__(self):
# 		print('Hello World!!! I am constructor')

# # instance 
# car = Car()


# class Vehicle:
# 	def __init__(self):
# 		print("Vehicle created")

# 	def __del__(self):
# 		print('Destructor called, vehicle deleted')

# vehicle = Vehicle()
# print("Hello World!! after Destructor")


'''
multiple constructors
'''
class Man:
	def __init__(self):
		print("I'm default Constructor of Man")
	# @classmethod
	# def eye(cls,color,shape):
	# 	cls.color = color
	# 	cls.shape = shape
	# 	print("In first def",color)
	@classmethod
	def eye(cls,shape,color):
		cls.shape = shape
		cls.color = color
		print("In second def",shape,",",color)
man = Man()

ob2 = Man.eye("round","brown")
ob1 = Man.eye("black","triangle")


