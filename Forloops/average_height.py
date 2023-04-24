'''This program should calculate the average height of the list of students'''

student_lst = input("Enter student height: ").split()
for num in range(0, len(student_lst)):
    student_lst[num] = int(student_lst[num])
#print(student_lst)



#get total height of students
total_height = 0
for height in  student_lst:
    total_height += height

#print(total_height)

#get the total number of students
total_num = 0
for number in student_lst:
    total_num += 1
#print(total_num)

#get the average 
average_height = total_height / total_num
#print(average_height)

#round to the nearest number
final_average = round(average_height)
print("AVERAGE HEIGHT = {}".format(final_average))