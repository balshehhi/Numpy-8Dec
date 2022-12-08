# 08-Dec NumPy topic

import numpy as np
#1D
"""
arr=np.array([1,2,3,4,5])
print (arr)
print(type (arr)) #<class 'numpy.ndarray'>
print(arr.ndim) # 1 ,means 1dimentional  array
print(arr.shape) # (5,) 5 coloum 
print(arr.size) # 5 element 
"""

# 3 D array
"""
arr = np.array([[[2, 3, 4, 5, 6], [3, 4, 55, 66, 77]], [[2, 3, 4, 5, 6], [3, 4, 55, 66, 77]]])
print(arr)
print(type(arr))

print(arr.ndim)
print(arr.shape)
print(arr.size)

"""


#4D array
"""
#arr = np.array([[[[2, 3, 4], [3, 4, 55]], [[2, 3,1], [3, 4, 55]]]])
#arr = np.array([[[[2,3,4,5,6],[3,4,5,6,9],[1,2,3,4,5]],
                [[2,3,4,5,6],[3,4,5,6,9],[1,2,3,4,5]]]
                ,
                [[[2,3,4,5,6],[3,4,5,6,9],[1,2,3,4,5]],
                [[2,3,4,5,6],[3,4,5,6,9],[1,2,3,4,5]]]
                ])
#arr=np.array([[[[2,3,4]]]])
arr=np.array([2,3,4], ndmin = 4)
print(arr)
print(type(arr))

print(arr.ndim)
print(arr.shape)
print(arr.size)
"""

#sliciing extract 41 , get 21,31,41,51,61   get  55,66, get  alternate items skip 1 element do reverse order
arr = np.array([[[2,3,4,5,6], [3,4,55,66,77]] ,[[21,31,41,51,61], [33,42,55,662,772]] ])
print(arr)
#print(arr[0]) #[[ 2  3  4  5  6]  [ 3  4 55 66 77]]
#print(arr[1]) # [[ 21  31  41  51  61]  [ 33  42  55 662 772]]
#print(arr[0][1]) #[ 3  4 55 66 77]
#print(arr[1][0]) # [21 31 41 51 61]
print(arr[1][0][2])   # extract 41 (1) first row  (2)3rd coloum
print(arr[1][1][2]) # extract 55
print(arr[1][0][0])  # give me 21 which is a first element
#print(arr[0][1][2:4]) # get  55,66
#print(arr[::2])
#print(arr[::-1]) # reverse order [[[ 21  31  41  51  61]  [ 33  42  55 662 772]] [[  2   3   4   5   6]  [  3   4  55  66  77]]]
#[9:58 AM] Ali Abdulsalam Alhosani
#print(arr[::2])
#print(arr[0:, 0:, 0:5:2])

