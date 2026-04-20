#----------task 1----------

name = input('Enter your name: ')
num_subjects = int(input('How many subjects do you have? '))

total_marks = 0

for i in range(1, num_subjects + 1):
    marks = float(input(f'Enter marks for subject {i} out of 100: '))
    total_marks = total_marks + marks

percentage_result = total_marks / num_subjects

if percentage_result >= 90:
    grade = 'A'
elif percentage_result >= 80:
    grade = 'B'
elif percentage_result >= 70:
    grade = 'C'
elif percentage_result >= 60:
    grade = 'D'
else:
    grade = 'F'

#----------result----------
print("----------Task 1----------")
print("Name:", name)
print("Percentage:", percentage_result)
print("Grade:", grade)
print("----------end of Task 1----------")
#----------end of task 1----------

