import numpy as np
# #using np.array() function to create a numpy array
# a1 = np.array([1,2,3])#1D array
# a2 = np.array([[1,2,3],
#               [4,5,6]])#2D array
# a3 = np.array([[[1,2,3],
#                 [4,5,6]],
#                [[7,8,9],

#                 [10,11,12]]])#3D array

# print(a1)
# print(a2)
# print(a3)

# #using numpy functions to create arrays
# a4 = np.zeros((3,3))#3x3 array of zeros
# a5 = np.ones((4,4))#4x4 array of ones
# a6 = np.arange(0,11)#1D array of numbers from 0 to 10
# print(a4)
# print(a5)
# print(a6)

# #indexing in numpy arrays
# arr = np.arange(10,110,10)#1D array of numbers from 10 to 100 with step size of 10
# print(arr)
# print(arr[0])#first element 
# print(arr[1])#second element
# print(arr[-1])#last element
# arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])#2D array
# print(arr1[0,0])#first row first column
# print(arr1[1,0])#second row first column
# print(arr1[2,0])#third row first column

# #slicing in numpy arrays
# arr2 = np.array([[[1,2,3,4,5],
#                  [6,7,8,9,10]],
#                  [[11,12,13,14,15],
#                  [16,17,18,19,20]],
#                  [[21,22,23,24,25],
#                  [26,27,28,29,30]]])#3D array

#advanced indexing in numpy arrays
a = np.array([10,20,30,40,50])
idx = np.array([1,2,3])#index array
print(a[idx])#output: [20 30 40]

cond = a>20
print(a[cond])#output: [30 40 50]

#basic operations on numpy arrays
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
print(x+y)#output: [ 7  9 11 13 15]
print(x-y)#output: [-5 -5 -5 -5 -5]
print(x*y)#output: [ 6 14 24 36 50]
print(x/y)#output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

#unary operations on numpy arrays
arr3 = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.sum(arr3))#output: 55
print(np.mean(arr3))#output: 5.5
print(np.median(arr3))#output: 5.5 for odd number of elements, median is the middle element, for even number of elements, median is the average of the two middle elements
print(np.std(arr3))#output: 2.8722813232690143
print(np.var(arr3))#output: 8.25 
#mean is the average of all the elements, median is the middle element, std is the standard deviation, var is the variance
#variance is the average of the squared differences from the mean,
# formula: var = sum((x - mean)^2)/n, where x is each element, mean is the average of all elements, and n is the number of elements
#standard deviation is the square root of variance
