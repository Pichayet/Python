import numpy as np
m = int(input("how many row do you want? : "))
A = np.ones([m,m])                                  # Make square matrix 
for k in range(m):                                  # Run Round Check
    for i in range(m):                              # Run Rows
        for j in range(m):                          # Run Columns
            if (i == j): 
                A[i,j] = 1
            elif (i < j): 
                A[i,j] = A[i,j-1] + A[i+1,j]
            elif (i > j):
                A[i,j] = A[i-1,j] + A[i,j+1]
print("The Matrix",m,"x",m," is :")
print(A)