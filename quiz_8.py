import numpy as np
m = int(input("how many row do you want? : "))
n = m  # Square matrix
i = 0  # Start index
j = 0  # Start index
A = np.zeros([m,n]) # Make square matrix 
print("Example for make square matrix")
print(A)
for i in range(i,m):
    j = 0 # Reset data for start new loop
    for j in range(j,n):
        if ((i < j)and(j != m)): 
            A[i,j] = 0  # replace 0 in index[i,j]
        elif ((i == j)or(j == m)): 
            A[i,j] = 1  # replace 1 in index[i,j]
        else:
            A[i,j] = -1 # replace -1 in index[i,j]
            
print("The Matrix",m,"x",n," is :")
print(A)