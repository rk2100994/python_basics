A = 3
B = 4

#logical operators
print("and",A and B)
print("or",A or B)
print("not", not A)

#identity operators

tuesday = 'yoga_day'
wednesday  = 'gym_day'

print(tuesday is 'gym_day')
print(wednesday is 'gym_day')
print(tuesday is not 'gym_day')

#membership operators (works on lists as well as dictionaries)
A = [1,2,3,4,5]

print(6 in A)

A_dict = {'Age':24}
print('Age' in A_dict)