### Introduction to Numpy
#import numpy
import numpy as np
#from numpy import array
import time
import scipy.sparse as sparse

#### Numpy Arrays
### Initializing Arrays
### Arrays can have any number of dimensions, and can be initalized in a variety of ways. The code below shows how to initialize arrays a length 3 one-dimensional array in various ways.
##a = np.array([1, 2, 3])
##b = np.ones((3,))
##c = np.zeros((3,))
##print(a)
##print(b)
##print(c)
##
### For multi-dimensional arrays, we simply add the sizes of the other dimensions. You can have as many dimensions as you like.
##d = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2D array of size 2x5, initialized manually
##e = np.ones((2,5))  #2D ones array of size 2x5
##f = np.zeros((2,5,8)) #3D zeros array of size 2x5x8
##g = np.random.rand(2,5) #Random 2D array of size 2x5
##print('d:',d)
##print('e:',e)
##print('f:',f)
##print('g:',g)
##
### The values of arrays are referenced with square brackets. Python starts with zero as the first index (contrary to, e.g., Matlab, which starts indexing at 1).
##x = np.random.rand(3, 5)
##print('x:',x)
##print(x[0,0])
##print(x[0,1])
##print(x[1,0])
##x[0,0] = np.pi
##print('new x:',x)
##
###Slicing Arrays
##A = np.random.rand(5,3)
##print('A:',A)
##print('first column of A:', A[:,0]) #First column of A
##print('first row of A:', A[0,:]) #First row of A

### To extract only some of the entries in a given column or row of an array, the indexing notation "a:b:c" can be used. Generally this means start indexing at a,
### increment by c, and stop before you get to b. It is important to note that b is not included in the range of indexing.
### Some important points: If a is ommitted, it is taken as 0. If b is ommitted, the indexing goes to the end of the array.
### If any numbers are negative, the array is treated as periodic.Examples are given below. It is a good idea to master this type of indexing, as it is used very often in Numpy.
##a = np.arange(20)
##print('a:',a)
##print('element of a from 0th to 6th:',a[0:7])
##print('element of a from 7th to the end:',a[7:])
##print('element of a from 10th to 2 element before the end:',a[10:-2])  #Note the -2 means 2 before the end of the array
##print('element of a from the beginning to the end with 2 increment size:',a[::2])

### We can mix the indexing above with slicing 2D or 3D arrays.
##A = np.reshape(np.arange(30),(3,10))
##print(A)
##print(A[:,::2])
##print(A[0:2,:])
##print(A[0,:])
##print(A[:,3])

### Logical Indexing
##A = np.random.rand(3,5)
##print(A)

##
##I = A > 0.5  #Boolean true/false
##print(I)
##A[I] = 10
##A[~I] = 0  #The ~ negates a boolean array
##print(A) 

### Operations on Numpy arrays
###Let's make two long lists that we wish to add elementwise
##n = 100000
##A = n*[1]
##B = n*[2]
##print('A=',end='');print(A)
##print('B=',end='');print(B)
##
###Let's add A and B elementwise using a loop in Python
##start_time = time.time()
##C = n*[0]
##for i in range(n):
##  C[i] = A[i] + B[i]
##print('C=',end='');print(C)
##python_time_taken = time.time() - start_time
##print("Python took %s seconds." % python_time_taken)
##
###Let's convert to Numpy and add using Numpy operations
##A = np.array(A)
##B = np.array(B)
##
##start_time = time.time()
##C = A + B
##numpy_time_taken = time.time() - start_time
##print("Numpy took %s seconds." % (numpy_time_taken))
##
##print('Numpy was %f times faster.'%(python_time_taken/numpy_time_taken))
##
##
###Matrix Multiplication using Numpy
##A = np.random.rand(3,5)
##B = np.random.rand(3,5)
##print(A)
##print('A*B=',end='');print(A*B)  #elementwise multiplication
##print('A-B=',end='');print(A-B)  #elementwise subtraction
###Examples of matrix multiplication and matrix/vector multiplication
##print('A@B.T=',end='');print(A@B.T)   #B.T means the transpose of B
##C = np.random.rand(5,7)
##D = np.ones((5,))
##print(D)
##print('A@C=',end='');print(A@C)
##print('A@D=',end='');print(A@D)


### Matrix Type Data
##A = np.random.rand(3,3)
##x = np.random.rand(3,1)
##print(A)
##print(x)
##print(A@x)
##
##A = np.matrix(A)
##print(A)
##print(A*x)
##
##A = sparse.csr_matrix(A)
##print(A)
##print(A*x)

###Most other operations work fine with Numpy arrays, and work elementwise. This includes the power operation  ∗∗ , and any special functions in Numpy. Some examples are below.
##A = np.reshape(np.arange(10),(2,5))
##
##print(A)
##print(A**2) #Square all elements in A
##print(np.sin(A)) #Apply sin to all elements of A
##
###Pretty much any function you may want to apply to a matrix has a built-in Numpy function to do the job, and as per the discussion above, this is much faster than writing a loop to do it in Python. Examples below.
##A = np.reshape(np.arange(30),(3,10))
##
##print(A)
##print(np.sum(A))   #Sums all entries in A
##print(np.sum(A,axis=0))  #Sums along axis=0, so it reports column sums
##print(np.sum(A,axis=1))  #Row sums
##print(np.mean(A,axis=0))  #mean along axis=0, so it reports column means
##print(np.mean(A,axis=1))  #Row mean
##print(np.median(A,axis=0))  #median along axis=0, so it reports column medians
##print(np.median(A,axis=1))  #Row median

### Broadcasting
##A = np.reshape(np.arange(30),(3,10))
##print(A)
##
##x = np.ones((10,))
##print(A+x) #Adds the row vector of all ones to each row of A
##
### Suppose we wanted to add a column vector to each column of A. The code below fails, why?
##A = np.reshape(np.arange(30),(3,10))
##print(A)
##
##x = np.ones((3,))
##print(x)
##print(x[:,np.newaxis])
##print(A+x[:,np.newaxis])
#print(A+x) #Adds the row column of all ones to each column of A
# Returns: operands could not be broadcast together with shapes (3,10) (3,)
# Reason: We are adding row vectors
# Answer: For broadcasting, the sizes of the last dimensions must macth up. Above they are 10 and 3, which are not compatible,
# wheras in the first example they were 10 and 10. To fix this, you can add a dummy axis to x, to make the last dimensions match up, using np.newaxis.

# Exercise 1:
def find_norm(v):
    array_v = np.array(v)
    norm = (np.sum(array_v**2))**(1/2)
    return norm

def largest_eigenvalue_magnitude(A, b_0, N):
    A_array = np.array(A)
    b_n = np.array(b_0)
    if A_array.shape[0] != A_array.shape[1]:
        print('Your matrix is not a square matrix, the definition of eigenvalues are defined only for square matrices!')
    else:
        for i in range(N):
            b_n = (A_array @ b_n)/find_norm(A_array @ b_n)
        eigenvalue = find_norm(A_array @ b_n)
        return eigenvalue
# The algorithm indeed works, check with some matrices over here: https://tutorial.math.lamar.edu/classes/de/la_eigen.aspx

# Exercise 2:
def approximate_pi(dx):
    dx = dx
    x = np.arange(0,1,dx)  #Array of numbers starting at 0, ending before 1, and incrementing by dx
    pi = 4*(np.sum(np.sqrt(1 - x**2)*dx))
    print(pi)
# Note that depending on the dx we choose, the lower the dx is, the more accurate our approximation is.
# Moreover, note that the amount of decimals that we approximate correctly is one to one related to the decimal point we choose for dx. In particular, 0.01 represent one decimal point accurate, 0.001 represent two decimal point accurate and so on.
