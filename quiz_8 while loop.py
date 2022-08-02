import numpy as np
m = int(input("how many row do you want? :"))
n = m
i = 0
j = 0
A = np.zeros([m,n],dtype=int)
print(A)
while ((i < (m-1))or(j < (m-1))):
    if ((i < j)and(j != m)):
        A[i,j] = 0
        j = j + 1 
        print(A)
        
    elif ((i == j)or(j == m)):
        A[i,j] = 1
        j = j + 1 
        print(A)
       
    else:
        A[i,j] = -1
        j = j + 1
        print(A)


print("Matrix :")
print(A)
          