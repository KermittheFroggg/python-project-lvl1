import prompt
import random


def calc(name_game):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    sign = [' + ', ' - ', ' * ']
    sym = random.choice(sign)
    print('Question: ' + str(number1) + sym + str(number2))
    answer = prompt.string('Your answer: ')
    if sym == ' + ':
        res = answer == str(number1 + number2)
        answer2 = number1 + number2
    elif sym == ' - ':
        res = answer == str(number1 - number2)
        answer2 = number1 - number2
    elif sym == ' * ':
        res = answer == str(number1 * number2)
        answer2 = number1 * number2
    return res, answer, answer2
