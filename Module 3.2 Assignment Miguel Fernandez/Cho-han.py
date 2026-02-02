#Miguel Fernandez Brazon
# 02/01/26
# Module 3.2 Assigment

import random, sys

# Japanese names for the dice
JAPANNumbers = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, modified by Miguel

dice game. You guess if the total is even {cho}
or odd {han}.

BONUS: If the total is 2 or 7, you get 10 mon.
''')
#Initial Money
purse = 7000
#Loop
while True:
    print('You Got', purse, 'mon. How much you want to bet? {or QUIT}')

    #user input bet
    while True:
        Game = input('mTT: ')
        if Game.upper() == 'QUIT':
            print('Thanks')
            sys.exit()
        elif not Game.isdecimal():  # check if number
            print('enter a number.')
        elif int(Game) > purse:  # can't bet more than your balance
            print('You do not have enough')
        else:
            Game = int(Game)
            break

    # roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('CHO (even) or HAN (odd)?')

    # cho or han
    while True:
        bet = input('mTT: ').upper()
        if bet not in ('CHO', 'HAN'):
            print('enter CHO or HAN.')
        else:
            break

    # show dice
    print('The dealer shows the dice:')
    print('  ', JAPANNumbers[dice1], '-', JAPANNumbers[dice2])
    print('    ', dice1, '-', dice2)

    total = dice1 + dice2

    # bonus rule
    if total == 2 or total == 7:
        print('BONUS! Total is', total, 'get 10 mon WHEE!')
        purse += 10  # add bonus

    # even or odd
    RollEven = (total % 2 == 0)
    correctBet = 'CHO' if RollEven else 'HAN'

    #see if win or loose
    if bet == correctBet:
        print('You won! You got!', Game, 'mon.')
        purse += Game

        #12%
        Game_fee = int(Game * 0.12)
        print('The Game collects a', Game_fee, 'mon fee.')
        purse -= Game_fee
    else:
        print('You lost Whoo!')
        purse -= Game

    # check if broke
    if purse == 0:
        print('Dont have money')
        print('Thanks for tryng :v !')
        sys.exit()