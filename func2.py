

print("toplevel in func2")


if __name__ == "__main__":
	print("func2 is directly run")
else:
	print("fun2 is being imported by another module")

#try running copying below line to top, this will work in flow where it is imported
import func1
func1.func1(8,8)
