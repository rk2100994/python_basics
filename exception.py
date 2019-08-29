import sys
list_ran = ['a',0,2]

for i in list_ran:
	try:
		print("Entry ele:", i)
		rec = 1/int(i)
		break
	except:
		print("Oops!",sys.exc_info()[0],"occured")
print("Reciprocal of entry is ",rec)