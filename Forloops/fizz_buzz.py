'''HERE WE HAVE A FIZZBUZZ GAME
In this program... the program should print numbers between
1 and 100 inclusive of both 1 and 100

if a number is divisible by 3 it should print fizz
if a number is divisible by 5 it should print buzz
if a number is divisible by both it should print fizzbuzz

'''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ", end=" ")
    elif number % 3 == 0:
        print("FIZZ", end=" ")
    elif number % 5 == 0:
        print("BUZZ", end=" ")
    else:
        print(number, end=" ")