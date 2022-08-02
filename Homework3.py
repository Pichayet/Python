name = input("What is your name : ")
print("Hello",name,"input more than 1 stick to start the game.")
N = int(input("How many stick (N) in the pile : "))
print("There are",N,"sticks in the pile.")
round = 0
import random
random = random.randint(1,2)
while N > 0 :                   #N = number of sticks
    if(round % 2 == 0 ):        #smart computer turn
        if(N == 1) :            #smart computer lose
            print("I,smart computer, take the last stick.")
            print(name,"win (I,smart computer,am sad T_T)")
        elif(2 <= N <= 12):     #smart computer control pick
            if(N == 3 or N == 6 or N == 9 or N == 12):  #pick 2
                print("I,smart computer ,take : 2 -----")
                print("There are ",N-2,"sticks in the pile.")
                N = N - 2
            else:               #pick 1
                print("I,smart computer ,take : 1 -----")
                print("There are ",N-1,"sticks in the pile.")
                N = N - 1
        else :                  #smart computer random
            print("I,smart computer ,take : ",random)
            if(N-random == 0):  #smart computer lose
                print("I,smart computer, take the last stick.")
                print(name,"win (I,smart computer,am sad T_T)")
            else:               #past next turn
                print("There are ",N-random,"sticks in the pile.")
                N = N-random
        round = round + 1 
        
    else:                       #player turn
        print(name,",",end="")
        S = int(input("How many sticks you will take(1-2) :"))
        if((S==1 or S==2)and(N>=S)): #player pick 1-2 sticks
            N = N-S
            round = round + 1
            if(N > 0):          #past next turn
                print("There are",N,"sticks in the pile.")          
            elif(N == 0):       #player lose
                print(name,"takes the last stick") 
                print("I,smart computer,win !!!")   
        elif((S==1 or S==2)and(N<S)):   #enough sticks
            print("There are no enough sticks to take.")
        elif(S>2):              #pick more 2 sticks
            print("No you cannot take more than 2 sticks!")
        else:                   #pick less 2 sticks
            print("No you cannot take more less than 1 stick!")