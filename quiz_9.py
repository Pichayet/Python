M = []
m = int(input("How many number do you want ?:"))
for i in range(0,m):
    number = int(input("What a number do you want ?:"))
    while(number < 0):
        print("You can't not input negative number,pls try again.")
        number = int(input("What a number do you want ?:"))
    M.append(number)   
print("List before sort :",M)
count_i = len(M)
count_j = len(M)
#print("i1 : ",i)
i = 0
#print(count)
#print("M1 : ",M)
#print("P1 : ",P)
M.sort(reverse=True)
#print("M2 : ",M)    
for i in range(0,count_i):
    #print("Round i :",i,"----------------------------")
    #print(M[i])
    #print(M[i+1])
    for j in range(0,count_j):
        print("Round j :",j)
        if(j != count_j-1):
            if(M[j]>=100 and M[j+1]<100):           #Case 1 [>=100] with [<=100]
                print("Case 1")
                if(M[j+1] >= 10):                   #Case 1.1 [>=100] with [>=10]
                    print("Case 1.1")
                    M1 = M[j]/100
                    M2 = M[j+1]/10
                    print("M1 :",M1)
                    print("M2 :",M2)
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [>=10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):       #digit of [>=100] equal digit of [>=10]
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        print("M4 : ",M4)
                        print("M5 : ",M5)
                        if(M4 <= M5):               #Decimal [>=100] minimum than digit of [>=10]
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                else:                               #Case 1.2 [>=100] with [<10]
                    print("Case 1.2")
                    M1 = M[j]/100
                    M2 = M[j+1]
                    if(int(M1) < int(M2)):          #digit of [>=100] minimun than digit of [<10]
                        print("Case 1.2.1")
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):       #digit of [>=100] equal digit of [<10]
                        print("Case 1.2.2")
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        M6 = M[j+1]/10
                        print("M4 : ",M4)
                        print("M5 : ",M5)
                        print("M6 : ",M6)
                        if(M4 <= M[j+1]/10):        #digit M[i] <= digit M[i+1]
                            print("Case 1.2.2.1")
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                        elif(M4 <= M5):             #
                            print("Case 1.2.2.2")
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
            elif(10 <= M[j] < 100 and M[j+1]<100): #Case 2 [10<=M[i]<100] with [<=100]
                #print("Case 2")
                if(M[j+1] >= 10):           #Case 2.1 [10<=M[i]<100] with [>=10]
                    #print("Case 2.1")
                    M1 = M[j]/10
                    M2 = M[j+1]/10
                    #print("M1 :",M1)
                    #print("M2 :",M2)
                    if(int(M1) < int(M2)):           #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        #print("M4 : ",M4)
                        #print("M5 : ",M5)
                        if(M4 <= M5):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                else:                       #Case 2.1 [10<=M[i]<100] with [<10]
                    #print("Case 2.2")
                    M1 = M[j]/10
                    M2 = M[j+1]
                    #print("M1 : ",M1)
                    #print("M2 : ",M2)
                    #print("int(M1) : ",int(M1))
                    #print("int(M2) : ",int(M2))
                    if(int(M1) < int(M2)):           #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                        #print("Case 2.2.1")
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        #print("M4 : ",M4)
                        #print("M5 : ",M5)
                        #print("Case 2.2.2")
                        if(int(M5) == 0):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                            #print("Case 2.2.2.1")
            elif(M[i] < 10 and M[j+1]<100): #Case 2 [10<=M[i]<100] with [<=100]
                #print("Case 3")
                if(M[j+1] >= 10):           #Case 2.1 [10<=M[i]<100] with [>=10]
                    #print("Case 3.1")
                    M1 = M[j]
                    M2 = M[j+1]/10
                    #print("M1 :",M1)
                    #print("M2 :",M2)
                    if(int(M1) < int(M2)):           #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        #print("M4 : ",M4)
                        #print("M5 : ",M5)
                        if(int(M5) != 0): 
                            if(M4 <= M5):
                                N = M[j]
                                M[j] = M[j+1]
                                M[j+1] = N
                else:                       #Case 2.1 [10<=M[i]<100] with [<10]
                    #print("Case 3.2")
                    M1 = M[j]
                    M2 = M[j+1]
                    if(int(M1) < int(M2)):           #digit of [>=100] minimun than digit of [<10]
                        N = M[j]
                        M[j] = M[j+1]
                        M[j+1] = N
                    elif(int(M1) == int(M2)):
                        M3 = int(M1)
                        M4 = float("{:.2f}".format(M1 - M3))
                        M5 = M2 - M3
                        #print("M4 : ",M4)
                        #print("M5 : ",M5)
                        if(M4 <= M5):
                            N = M[j]
                            M[j] = M[j+1]
                            M[j+1] = N
                
            print("Round :",count_j,"List :",M)
print("List after sort :",M)
M = map(str,M)
print("The largest formed number is :","".join(M))