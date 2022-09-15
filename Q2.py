text = input("Input a letter that you want to check a palindrome :")
length = len(text)
final_text = ""
reversed_text = ""
l = 0
r = length - 1
while (l < r) :                                             
    if (text[l] == text[r] and text[l+1] == text[r-1]) :    #Couple is the same
        r -= 1
    else :                                                  #Couple is not the same
        reversed_text = text[l] + reversed_text
    l = l + 1

final_text = text + reversed_text
print('The palindrome is :',final_text)