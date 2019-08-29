class Error(Exception):
	pass

class ValueSmallError(Error):
	pass

class ValueLargeError(Error):
	pass

number = 10

while True:
	try:
		in_num  = int(input("enter a number: "))
		if in_num < number:
			raise ValueSmallError
		elif in_num > number:
			raise ValueLargeError
		break
	except ValueSmallError:
		print("This is too small number, try again")
	except ValueLargeError:
		print("This is too large number, try again")
print("Congratulations!!! you guessed it correctly.")