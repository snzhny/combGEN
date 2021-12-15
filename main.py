# coding: utf-8
# team nekos
import string
import random

# плохой код могу объяснить
# много одинакового кода, то есть 
# 1) много повторов 
#      for i in range(100000):
#         j = False
#         while not j:
# 2) много повторов
#     if ran not in slovar:
#         j = True #???
#     else:
#         j = True #???
#         slovar.remove(ran)
# slovar.append(str(ran))


# uncorrect name variable
var = string.ascii_letters
#??? wtf in down
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
file = open('output.txt', 'w')
#check this constructor
#with open("output.txt", mode='w') as file: <<< attention !!!
word = input("Enter code word:")
print("After code word(number): ")
S = int(input())
slovar = []
ran = 0
side = input("Select the side where the line will be added: (1)LEFT, (2)RIGHT, on (3)BOTH sides: ").lower()
print("Just wait...")
# подними j на глобальный уровень много раз init 
#         j = False

# if side in ("1", "left"):
if side == "1" or side == "left":
    for i in range(100000):
        j = False
        while not j:
            prefix = ''.join(random.choices(string.ascii_letters + string.digits + word, k=S)) #combination generating
            ran = prefix + word
            
            # vaiable must be english language
            # slovar.remove(ran) if ran in slovar else print("go else")
            # j = True ??? 
            
            if ran not in slovar:
                j = True #???
            else:
                j = True #???
                slovar.remove(ran)
        slovar.append(str(ran))
        file.write(str(ran) + "\t")
# elif side in ("2", "right"):
if side == "2" or side == "right":
    for i in range(100000):
        j = False
        while not j:
            ran = word + ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            
            # vaiable must be english language
            # slovar.remove(ran) if ran in slovar else print("go else")
            # j = True ??? 
            
            if ran not in slovar:
                j = True #???
            else:
                j = True #???
                slovar.remove(ran)
        slovar.append(str(ran))
# elif side in ("3", "both"):
if side == "3" or side == "both":
    for i in range(100000):
        j = False
        while not j:
            prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            postfix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            ran = prefix + word + postfix

            # vaiable must be english language
            # slovar.remove(ran) if ran in slovar else print("go else")
            # j = True ??? 
            
            if ran not in slovar:
                j = True
            else:
                j = True
                slovar.remove(ran)
        slovar.append(str(ran))
# else:
# something if uncorrect input would be
        
print("Check your 'output.txt'")
