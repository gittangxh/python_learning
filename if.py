number = 30

guess = int(input('input your guessing number:'))

if guess == number:
    print('congratulations! you are right!')
elif guess < number:
    print('too small!')
elif guess > number:
    print('too big!')
print('it is over')
