# coding: utf-8
# team nekos
import string
import random

word = input("Enter code word:")
print("After code word(number): ")
S = int(input())
words = []
side = input("Select the side where the line will be added: (1)LEFT, (2)RIGHT, on (3)BOTH sides: ").lower()
print("Just wait...")

with open("output.txt", mode='w') as file:
    if side in ("1", "left"):
        for i in range(100000):
            j = False
            while not j:
                prefix = ''.join(random.choices(string.ascii_letters + string.digits + word, k=S)) #combination generating
                ran = prefix + word
                if ran not in words:
                    j = True
                else:
                    j = True
                    words.remove(ran)
            words.append(str(ran))
            file.write(str(ran) + "\t")
    elif side in ("2", "right"):
        for i in range(100000):
            j = False
            while not j:
                ran = word + ''.join(random.choices(string.ascii_letters + string.digits, k=S))
                if ran not in words:
                    j = True
                else:
                    j = True
                    words.remove(ran)
            words.append(str(ran))
            file.write(str(ran) + "\t")
    elif side in ("3", "both"):
        for i in range(100000):
            j = False
            while not j:
                prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
                postfix = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
                ran = prefix + word + postfix

                if ran not in words:
                    j = True
                else:
                    j = True
                    words.remove(ran)
            words.append(str(ran))
            file.write(str(ran))
    else:
        print("Incorrect Input")
print("Check your 'output.txt'")
