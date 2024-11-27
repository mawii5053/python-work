#eg 
#a college offers a course that prepares students pharmacy licensing test.
#the college wants to know how well its students did on the exam.
#write a programm to compute the result, a list of 10 students were given.
#write 1 if student passed and 2 if student failed. 

"""using nested control statement to analyze examination results"""

#initialize variables
passes = 0 # number of passes
failures = 0 # number of failures

# process 10 students
#for student in range(10):
    # get one exam result
    #result = int(input('enter result(1= pass, 2= fail):  '))
    #if result == 1:
        passes = passes + 1
   #else:
        failures = failures + 1
# termination phase
#print('passed:', passes)
#print('failed:', failures)

#if passes > 8:
    #print('bonus to malawii')

# using a for statement to input two integers
# using a nested if...else statemente to display whether each value is even or odd.
# enter 20 and 15 to test my code

for count in range(2):
    value = int(input('enter an integer:  '))
    if value % 2 == 0:
        print(f'{value} is even')
    else:
        print(f'{value} is odd')    
