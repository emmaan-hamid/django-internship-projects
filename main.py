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

#----------task 2----------

#----------odd numbers----------
def get_odds(numbers):
    odds = []
    for number in numbers:
        if number % 2 != 0:
            odds.append(number)
    return odds

#----------even numbers----------
def get_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

#----------prime numbers----------
def get_primes(numbers):
    primes = []
    for number in numbers:
        if number <=1:
            continue
        isPrime = True

        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(number)
    return primes


numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))

odds = get_odds(numbers)
evens = get_evens(numbers)
primes = get_primes(numbers)

if odds:
   print("Odd numbers:", odds)
else:
    print("Odd number not found")

if evens:
    print("Even numbers:", evens)
else:
    print("Even number not found")

if primes:
    print("Prime numbers:", primes)
else:
    print("Prime number not found")
#----------end of task 2----------

#----------task 3----------

def withdraw(balance,amount):
    if amount > 0 and amount <= balance and amount % 500 == 0:
        balance = balance - amount
        print('Withdraw success! remaining balance:', balance)
    else:
        print('Withdraw failed!')
    return balance

pin = '7890'
balance = 4500

entered_pin = input('Enter your pin: ')

if pin != entered_pin:
    print('Wrong pin entered!')
else:
    amount = float(input('Enter your amount to withdraw: '))

    if amount == 0:
        print('Nothing to Withdraw! remaining balance:', balance)

    balance = withdraw(balance,amount)
#----------end of task 3----------
