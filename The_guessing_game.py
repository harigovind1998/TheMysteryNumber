import random
randnum = random.randint(0,20)
number_of_try= 0
name = input('Please input your name to begin the game: ')
nameinp = False
while not nameinp:
    if name != '':
        name = name.capitalize()
        print(name)
        print('Hello ' + name + ' I have randomly chosen a number between 0 and 20, care to take a guess? You have 5 tries to successfully guess the mystery number!')
        nameinp = True 
        break 
    else:
        name = input('please enter a valid name:')
while number_of_try <6:
    guess = int(input("Choose a number between 0 and 20: "))
    number_of_try += 1
    if guess < randnum:
        print("sorry your number is too low")
    elif guess > randnum:
        print("sorry your number is too high")
    else:
        print("good job")
        break
if guess == randnum:
    print('Congrats, you guess the correct number in, ' + str(number_of_try) + ' try(s)')
if guess != randnum: 
    print('Sorry you were unable to guessed the correct number, the mystery number was ' + str(randnum) + ' Good luck next time!')
    
    