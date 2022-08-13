# -*- coding: utf-8 -*-
"""Quiz 6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ug_9xxVeFE6ny2Vk35ze2msGFp2DT3Cb
"""

Morse ={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 
         'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
         'S':'...', 'T':'-', 'U':'..-','V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', 
         '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

Text = input("What text do you want to translate to morse code :")
Text = Text.upper()
row = ""
for c in Text :
    morse = Morse[c]
    row = row + " " + morse
print(row)