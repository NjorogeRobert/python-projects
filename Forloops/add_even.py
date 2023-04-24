'''THIS PROGRAM WILL ADD ALL THE EVEN NUMBERS BETWEEN 1 AND 100
INCLUDING 1 AND 100
'''
even = 0
for number in range(1, 101):
    if number % 2 == 0:
        even += number

print("THE TOTAL OF ALL EVEN NUMBERS IS {}".format(even))
