binary = input('binary string(between 3-20 bits) :')
Len_binary = len(binary)
while (3 < Len_binary > 20):                                    
    print("Pls input binary less than 20 bits")
    binary = input('binary string :')
    Len_binary = len(int(binary))
for i in binary:                                                #ตรวจสอบว่าเป็นจำนวนเต็มหรือป่าว
    if (i == ".") :                                                 #เงื่อนไขแบบมีจุด
        B1,B2 = binary.split(".")
        total = B1 + B2
        total_sort = sorted(total,reverse = True)
        print('Total_sort',total_sort)
        break
    else :                                                          #เงื่อนไขแบบไม่มีจุด
        total = binary
        total_sort = sorted(total,reverse = True)
        print('Total_sort',total_sort)
for i in total_sort:                                            #ตรวจสอบว่ามีเลขมากกว่า 1 ไหม
    while(0 < int(i) >= 2):                                             #มีเลขมากกว่า 2 (ใส่ใหม่)
        print("pls input binary")
        binary = input("Enter the binary string :")
        for i in binary:
            if (i == "."):                                              #เงื่อนไขแบบมีจุด
                B1,B2 = binary.split(".")
                total = B1 + B2
                total_int = int(total)
                print(type(total_int))
                total_sort = sorted(total,reverse = True)
                print('Total_sort',total_sort)
                i = total_sort[0]
                break
            else :                                                      #เงื่อนไขแบบไม่มีจุด
                total = binary
                B1 = binary
                total_sort = sorted(total,reverse = True)
                print('Total_sort',total_sort)
                i = total_sort[0]
    break

number_5 = '101'
count = 0
for i in range(0,Len_binary) :
    if(int(number_5) == int(binary[i:i+3])):
        count = count + 1
    
print(count)





