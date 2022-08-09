M = []
P = []
m = int(input("How many number do you want ?:"))
for i in range(0,m):
    number = int(input("What a number do you want ?:"))
    if(number < 0):
        print("You can't not input negative number,pls try again.")
        i = i - 1
    M.append(number)
    P.append(number)
count = len(M)
#print("i1 : ",i)
i = 0
#print(count)
#print("M1 : ",M)
#print("P1 : ",P)
for i in range(0,count):
    if(M[i] < 10):
        M[i]
    elif(10 <= M[i] <= 100):
        result = M[i]/10
        M[i] = result         
    else:
        result = M[i]/100
        M[i] = result        
M.sort(reverse=True)       
print("M2 : ",M)    
for i in range(0,count):
    #print(i)
    #print(M[i])
    if(i != count-1):
        if(int(M[i]) == int(M[i+1])):
            #print(M[i])
            #print(M[i+1])
            N = M[i] - int(M[i])
            N1 = M[i+1] - int(M[i])
            #print(N)
            #print(N1)
            #print(int(M[i])/10)
            if(N >= (int(M[i])/10)):
                M[i] = M[i]
                #print("1",M[i])
            elif(int(N) == int(N1)):
                M[i] = M[i]
                #print("2",M[i])
            else:
                O = M[i]
                M[i] = M[i+1]
                M[i+1] = O
                #print("3",M[i])
                
i = 0
j = 0
print(type(M[2]))
#print("i2 : ",i)
print("M3 : ",M)
#print("P2 : ",P)
for i in range(0,count):
    #print("i2 : ",i)
    for j in range(0,count):
        print("M[i]",M[i],"   ""P[j]",P[j])
        if(M[i] == P[j]/10 and type(M[i] == float)):
            M[i] = int(M[i] * 10)
            #print(j , "1 " ,M[i])
        elif(M[i] == P[j]/100 and type(M[i] == float)):
            M[i] = int(M[i] * 100)
            #print(j , "2 " ,M[i])
        else:
            M[i] = M[i]
            #print(j , "3 " ,M[i])
        print("M test :",M)
print("M4 : ",M) 
print("P3 : ",P)              
M = map(str,M)
print("".join(M))