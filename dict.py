A = {'Age':24,'Country':'India'}
print(A)
print(A['Age'])
print("***NEXT***")

B = {'Age':34,'Cage':5,'Bage':56}
value1 = []
sorted_dict = {}
for key,val in B.items():
	# print(key,",",val)
	value1.append(val)
	# print(value1)
print(sorted(value1))
for name, age in B.items(): 
	# print(name,",",age)
	for i in sorted(value1):
		if i == age:
			sorted_dict[name] = i
print(sorted_dict)