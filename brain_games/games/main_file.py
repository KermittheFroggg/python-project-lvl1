import prompt
from brain_games.games.calc import calc
from brain_games.games.gcd import gcd


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name != '':
        print('Hello, ' + name + '!')
    return name


def start_game(name_game):
    name = welcome_user()
    if name_game == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif name_game == 'calc':
        print('What is the result of the expression?')
    elif name_game == 'gcd':
        print('Find the greatest common divisor of given numbers')
    i = 1
    while i <= 3:
        if name_game == 'calc':
            res, answer, answer2 = calc(name_game)
        if name_game == 'gcd':
            res, answer, answer2 = gcd(name_game)
        if res:
            print('Correct!')
            if i == 3:
                print('Congratulations, ' + name + '!')
            i += 1
        else:
            text1 = ' is wrong answer ;(. Correct answer was '
            text2 = ". \nLet's try again, "
            print(answer + text1 + str(answer2) + text2 + name + "!")
            break
