#----------task 1----------

name = input('Enter your name: ')

sub1 = float(input('Enter your marks for sub 1 out of 100: '))
sub2 = float(input('Enter your marks for sub 2 out of 100: '))
sub3 = float(input('Enter your marks for sub 3 out of 100: '))
sub4 = float(input('Enter your marks for sub 4 out of 100: '))
sub5 = float(input('Enter your marks for sub 5 out of 100: '))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage_result = total_marks / 5

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

