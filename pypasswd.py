'''THIS PROGRAM GENERATES A PASSWORD
IT REQUESTS HOW MANY LETTERS YOU WOULD WANT
HOW MANY SYMBOLS YOU WOULD WANT
HOW MANY NUMBERS YOU WOULD WANT AND FINALLLY 
PRINTS THE PASSWORD
'''
import random
letter_num =int(input("How amny letters would you want in your password? "))
letters =['a','b','c','d','e','f']
letter =random.shuffle(letters)
for num in range(0, letter_num):
    print(letter[num], end="")