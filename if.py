number = 23
guess = int(input('enter an integer : '))

if guess == number:
    print('Congratulations, you guessed it')
    print('(but you do not win with any prizes!)')
elif guess < number:
    print('no,it is little higher than that')
else:
    print('no,is is little lower than that')
print('Done')
