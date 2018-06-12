# This program is developed by Pradeep Sahoo

# import numpy
from numpy import *

Z = "Pradeep Sahoo is done with HW2"

print(Z)


# Assigning random numbers
A = random.random(15)


# creation of Matrix
A = reshape(A,(3,5))
print (A)

# size of Matrix
size = A.size
print(size)

print(A[-3:-1])

# shape/length of Matrix
l = A.shape
print(l)

# creating  the Transpose and store 
B = A.T
print(B)

#minimum value in column 1 of matrix B
C = B.min(axis=0)
print(C)

#Minimum and maximum values for entire matrix A

G = A.max()
H = A.min()

print(G)
print(H)

#Create a Array with 4 random elements

X1 = 4
X = [random.random() for i in range(X1)]

print(X)

    
    







