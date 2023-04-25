'''THIS PROGRAM GENERATES A PASSWORD
IT REQUESTS HOW MANY LETTERS YOU WOULD WANT
HOW MANY SYMBOLS YOU WOULD WANT
HOW MANY NUMBERS YOU WOULD WANT AND FINALLLY 
PRINTS THE PASSWORD
'''
import random
print("WELCOME TO PASSWORD GENERATOR")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*', ')']
letter_num =int(input("How amny letters would you want in your password? "))
symbol_num = int(input("How many symbols? "))
num_number = int(input("How many numbers? "))

passwd = ""

for letter in range (0, letter_num):
    passwd += random.choice(letters)

for symbol in range(0, symbol_num):
    passwd += random.choice(symbols)

for num in range(0, num_number):
    passwd += random.choice(number)

print(passwd)

