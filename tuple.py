# This is immutable
tuple_lst = (1,2,3)

print(tuple_lst[0])
print(tuple_lst[1])
print(tuple_lst[2])

''' 
The below line give error as it is not possible to change
tuple_lst[2] = 4
error is   tuple_lst[2] = 4
TypeError: 'tuple' object does not support item assignment