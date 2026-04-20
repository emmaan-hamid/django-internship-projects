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
