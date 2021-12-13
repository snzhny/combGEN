# coding: utf-8
# team nekos
import string
import random

var = string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
file = open('output.txt', 'w')
word = input("Enter code word:")
print("After code word(number): ")
S = int(input())
slovar = []
ran = 0
side = input("Select the side where the line will be added: (1)LEFT, (2)RIGHT, on (3)BOTH sides: ").lower()
print("Just wait...")
if side == "1" or side == "left":
    for i in range(100000):
        j = False
        while not j:
            prefix = ''.join(random.choices(string.ascii_letters + string.digits + word, k=S)) #combination generating
            ran = prefix + word

            if ran not in slovar:
                j = True
            else:
                j = True
                slovar.remove(ran)
        slovar.append(str(ran))
        file.write(str(ran) + "\t")

if side == "2" or side == "right":
    for i in range(100000):
        j = False
        while not j:
            ran = word + ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            if ran not in slovar:
                j = True
            else:
                j = True
                slovar.remove(ran)
        slovar.append(str(ran))
if side == "3" or side == "both":
    for i in range(100000):
        j = False
        while not j:
            prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            postfix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
            ran = prefix + word + postfix

            if ran not in slovar:
                j = True
            else:
                j = True
                slovar.remove(ran)
        slovar.append(str(ran))
print("Check your 'output.txt'")
