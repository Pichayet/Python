binary = input("Enter the binary string :")
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
    print(i)
    while(int(i) >= 2):                                             #มีเลขมากกว่า 2 (ใส่ใหม่)
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
Length_B1 = len(B1)
result1 = 0
for i in total :
    D = 2**(Length_B1-1)*int(i)
    Length_B1 = Length_B1 - 1  
    result1 = result1 + D

print(result1)