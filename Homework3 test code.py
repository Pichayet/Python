name = input("What is your name : ")
print("Hello",name,"input more than 1 stick to start the game.")
N = int(input("How many stick (N) in the pile : "))
#print("There are",N,"sticks in the pile.")
T = int(input("How many stick (N) in the pile for last case : "))
R = int(input("How many round do you want to test : "))
Nnew = N
i = N
from random import randint
for i in range(i,T+1): 
    for j in range(1,R+1):
        print("round : " ,i)
        #print("Number of sticks : ",N,"  ",end="")
        round = 2
        while N > 0 :                   #N = number of sticks
            random = randint(1,2)
            if(round % 2 == 0 ):       #smart computer turn
                if(N == 1) :            #smart computer lose
                    #print("I,smart computer, take the last stick.")
                    print(name,"win (I,smart computer,am sad T_T)")
                    N = N - 1
                elif(2 <= N <= 12):
                    if(N == 3 or N == 6 or N == 9 or N == 7 or N == 12):
                        #print("I,smart computer ,take : 2 -----")
                        print("Bot -- There are",N-2,"sticks in the pile.")
                        N = N - 2
                    else:
                        #print("I,smart computer ,take : 1 -----")
                        print("Bot -- There are",N-1,"sticks in the pile.")
                        N = N - 1
                else :                  #smart computer random
                    #print("I,smart computer ,take : ",randint(1,2))
                    if(N-random == 0):  #smart computer lose
                        #print("I,smart computer, take the last stick.")
                        print(name,"win (I,smart computer,am sad T_T)") 
                    else:               #past next turn
                        random = randint(1,2)
                        print("Bot -- There are ",N- random,"sticks in the pile.")
                        N = N-random
                round = round + 1 
            else:                       #player turn
                if(N == 1):
                    N = 0
                    #print(name,"takes the last stick")
                    print("I,smart computer,win !!!")
                    round = round + 1
                elif((N>=0)): #player pick 1-2 sticks
                    #print(name,",",end="")
                    S = randint(1,2)
                    N = N - S
                    #print("How many sticks you will take(1-2) :",S)
                    round = round + 1
                    if(N > 0):          #past next turn
                        print("There are",N,"sticks in the pile.")   
                        N
                    elif(N == 0):       #player lose
                        #print(name,"takes the last stick") 
                        print("I,smart computer,win !!!") 
                      
        N = Nnew
        print("End-----------------------")
    Nnew = Nnew + 1
    N = Nnew    
    