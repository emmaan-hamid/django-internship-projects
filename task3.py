
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
