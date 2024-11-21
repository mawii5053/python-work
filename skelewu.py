#coding with algorithm
"""class average  program with sequence"""

#initialization phase
total = 0   #sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]  #list of 10 grades

#processing phase
for grade in grades:
    total += grade   #add current grade to the running total
    grade_counter += 1 #indicate that one more grade was processed

# termination phase
average = total / grade_counter
print(f'class average is {average}')

# implementaion of a sentinal- controlled iteration
"""class average program with sentinal-controlled iteration"""

# initialization phase
total = 0
grade_counter = 0

#processing phase
grade = int(input('enter grade, -1 to end:  ')) # get one grade

while grade != -1:
    total += grade
    grade_counter += 1
    grade = int(input('enter grade , -1 to end:  '))

# TERMINATION phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'class average is {average: .2f}')
else:
    print('no grades were entered')        