def func1(a,b):
	print("func() in func1.py")

print("toplevel in func1.py")

if __name__ == '__main__':
	print("func1.py directly run")
else:
	print("func1.py is being imported into another module")