# muj druhy projekt "Bulls and cows" game
import random
import time

ODDELOVAC = '=' * 56
first_rand = ['1', '2', '3', '4',
              '5', '6', '7', '8', '9']
rest_rand = ['0', '1', '2', '3', '4',
             '5', '6', '7', '8', '9']

genum = []
a = True

while a:
    first = random.sample(first_rand, 1)
    rest = random.sample(rest_rand, 3)
    genum = first + rest
    # print(genum)
    if len(set(genum)) == 4 and genum[0:1] != 0:
        genum = genum
        a = False

print("Hi there!",
      ODDELOVAC,
      "I've generated a random 4 digits number for you.",
      "Let's play \"Bulls and cows\" game.",
      ODDELOVAC,
      'Time is running, good luck !!!',
      sep='\n',
      end=f'\n{ODDELOVAC}\n')

victory = False
guesses = 0
t0 = time.time()

while not victory:
    guesses += 1
    NUMBER = input("Enter 4 unique digits: ")
    if len(NUMBER) < 4 or len(NUMBER) > 4:
        print('Enter number of exactly FOUR unique digits')
        break
    elif NUMBER[:1] == '0':
        print('The first digit must not be a zero.')
        break
    elif not NUMBER.isdecimal():
        print('Enter only digits, not characters')
        print(ODDELOVAC)
        break
    elif len(set(NUMBER)) < 4:
        print('Each of 4 digits must be unique')
        break

    bulls = 0
    cows = 0
    for i, num in enumerate(NUMBER):
        for i1, num1 in enumerate(genum):
            if (i, num) == (i1, num1):
                bulls += 1
            if bulls == 4:
                print(f'Amazing, you have'
                      f' guessed the right number '
                      f'in {guesses} guesses!')
                victory = True
            elif num == num1 and i != i1:
                cows += 1

    print(str(bulls) + ' bulls,' + str(cows) + ' cows'
          + f'{guesses}. guess'.rjust(36))
    print(ODDELOVAC)

t1 = (time.time() - t0)

if victory and guesses <= 5:
    print("*** You are THE MAGICIAN !!! ***".center(56))
elif victory and 5 < guesses < 10:
    print("*** Very good MASTER !!! ***".center(56, '*'))
elif victory and guesses > 10:
    print("You need to practice more  :) !!!".center(56))

print(ODDELOVAC)
print(f'Time elapsed:  {round(t1)} seconds.'.center(56))


