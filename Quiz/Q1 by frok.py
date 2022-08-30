import re
binary = input('binary string(between 3-20 bits :')
out = ""
binary = re.findall(r'[0-1]+', binary)
for e in binary :
    out = out + e
print(out)
Len_binary = len(out)
print(Len_binary)
while (3 < Len_binary > 20):
    print("Pls input binary less than 20 bits")
    binary = input('binary string : ')
    out = ""
    binary = re.findall(r'[0-1]+', binary)
    for e in binary :
        out = out + e
    Len_binary = len(out)
    print(out)
    
number_5 = '101'
count = 0
for i in range(0,Len_binary) :
    if(int(number_5) == binary[i:i+3]):
        count = count + 1
    
print(count)