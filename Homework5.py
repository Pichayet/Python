M = []
m = int(input("How many number do you want :"))
for i in range(0,m):
    number = int(input("What a number do you want :"))
    while(number < 0):
        print("You can't not input negative number,pls try again.")
        number = int(input("What a number do you want ?:"))
    M.append(number)
print("List before sort :",M)
count_i = len(M)
count_j = len(M)
i = 0
M.sort(reverse=True)
for i in range(0,count_i): #ลองเปลี่ยนเป็น len(M)
    for j in range(0,count_j):
        if(j != count_j-1):
            if(M[j]>=100 and M[j+1]<100):           #Case 1 [>=100] with [<=100]
                if(M[j+1] >= 10):                   #Case 1.1 [>=100] with [>=10]
                    M1 = M[j]/100
                    M2 = M[j+1]/10
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [>=10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):       #digit of [>=100] equal digit of [>=10]
                        M3 = int(M1)        
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3        
                        if(M4 <= M5):               #Decimal [>=100] minimum than digit of [>=10]
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                else:                               #Case 1.2 [>=100] with [<10]
                    M1 = M[j]/100
                    M2 = M[j+1]
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):       #digit of [>=100] equal digit of [<10]
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        M6 = M[j+1]/10
                        if(M4 <= M[j+1]/10):        #digit M[i] <= digit M[i+1]
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                        elif(M4 <= M5):             #
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
            elif(10 <= M[j] < 100 and M[j+1]<100):  #Case 2 [10<=M[i]<100] with [<=100]
                if(M[j+1] >= 10):                   #Case 2.1 [10<=M[i]<100] with [>=10]
                    M1 = M[j]/10
                    M2 = M[j+1]/10
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        if(M4 <= M5):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                else:                               #Case 2.1 [10<=M[i]<100] with [<10]
                    M1 = M[j]/10
                    M2 = M[j+1]
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        if(int(M5) == 0):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
            elif(M[i] < 10 and M[j+1]<100):         #Case 2 [10<=M[i]<100] with [<=100]
                if(M[j+1] >= 10):                   #Case 2.1 [10<=M[i]<100] with [>=10]
                    M1 = M[j]
                    M2 = M[j+1]/10
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        if(int(M5) != 0): 
                            if(M4 <= M5):
                                N = M[j]
                                M[j] = M[j+1]
                                M[j+1] = N
                else:                               #Case 2.1 [10<=M[i]<100] with [<10]
                    M1 = M[j]
                    M2 = M[j+1]
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        if(M4 <= M5):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
print("List after sort :",M)
M = map(str,M)
print("The largest formed number is :","".join(M))