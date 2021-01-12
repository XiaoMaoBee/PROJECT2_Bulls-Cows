# muj druhy projekt "Bulls and cows" game
import random
import time

ODDELOVAC = '=' * 56
list_rand = ['0', '1', '2', '3', '4',
             '5', '6', '7', '8', '9']


def generate_num() -> list:
    return random.sample(list_rand, 4)

generate_num()
genum = generate_num()

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
    print(f'{genum=}')
    NUMBER = list(input("Enter 4 digit number: "))
    if len(NUMBER) < 4 or len(NUMBER) > 4:
        print('''Enter number of exactly FOUR digits
Start again''')
        print(ODDELOVAC)
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

    print(f'{bulls} bulls, {cows} cows,({guesses}. guess)')
    print(ODDELOVAC)

t1 = (time.time() - t0)

if victory and guesses <= 5:
    print("*** You are THE MAGICIAN !!! ***".center(56))
elif victory and 5 < guesses < 10:
    print("*** Very good MASTER !!! ***".center(56, '*'))
elif victory and guesses > 10:
    print("What a waste of time :D !!!".center(56))

print(ODDELOVAC)
print(f'Time elapsed:  {round(t1)} seconds.'.center(56))


