import numpy as np 

a = np.array([1,2,3])
b = [2,3,4]
print("Numpy array",a)
print("Type of numpy array", type(a))
print("Original array",b)
print("Type of original array", type(b))

c = np.array([[1,2,5],[3,4]])
d = np.array([[1,5],[3,4]])
print("See the difference of below printed arrays dimessions")
# this difference is because of dimessions difference
print(c)
print(d)

#np array using range
e = np.arange(0,11)
print(e)

zeros = np.zeros((5,5))
print(zeros)
print("*****Another zeros*****")
zeros1 = np.zeros((3,4))
print(zeros1)

#linearly spaced vector
#linspace(start,stop,step)
#gives #steps values
#gives random values
vector = np.linspace(0,20,5)
print(vector)

vector1 = np.linspace(0,20,2)
print(vector1)

vector2 = np.linspace(0,20,10)
print(vector2)

#Restructuring a numpy array
arr = np.zeros(8)
print("Before array \n",arr)
arr_res = arr.reshape((2,2,2))
print("After array \n", arr_res)


#indexing and slicing
ar = np.arange(4,10)
ele = ar[2]
print(ar)
print("selected ele",ele)
print("type ele",type(ele))
print("addition",ele+7)
print("addition type",type(ele+7))
print("normal add type",type(7+5+7))

#slicing
abc = np.arange(0,20)
abc_slice = slice(1,10,2)
print(abc[abc_slice])

#slicing method2
# ab123 = np.array([1,2,3], [4,5,6],[7,8,9])
# print(ab123[1:,:2])

#numpy.empty creates an uninitialized array of specified shape and dtype
x = np.empty([3,2], dtype=int)
print(x)