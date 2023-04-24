'''CALCULATES THE MAXIMUM NUMBER IN A LIST WITHOUT THE USE OF MAX AND MIN FUNCTIONS
we shall calculate the highest score in a list
'''
student_scores = input("Input a list of student scores: ").split()

for num in range(0, len(student_scores)):
    student_scores[num] = int(student_scores[num])

#print(student_scores)

#TO GET THE MAXIMUM SCORE
maximum = student_scores[0]
for maxi in student_scores:
    if maxi > maximum:
        maximum = maxi

print("The highest score in the class is: {}".format(maximum))