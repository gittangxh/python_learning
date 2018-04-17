number = 30

running = True


while running:
    guess = int(input('input your guessing number:'))
    if guess == number:
        print('congratulations! you are right!')
        running = False
    elif guess < number:
        print('too small!')
    elif guess > number:
        print('too big!')
print('it is over')
