'''this program finds the highest number in a list of numbers'''

student_lst = input("Enter the age of students: ").split()
for num in range(0, len(student_lst)):
    student_lst[num] = int(student_lst[num])

print(student_lst)

#CALCULATE THE MAX AGE
maxi = student_lst[0]

for age in student_lst:
    if age > maxi:
        maxi = age

print("MAXIMUM AGE: = {}".format(maxi))