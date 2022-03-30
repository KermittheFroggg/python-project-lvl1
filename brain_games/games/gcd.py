import prompt
import random


def gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Question: ' + str(number1) + ' ' + str(number2))
    answer = prompt.string('Your answer: ')
    i = 1
    while i <= min(number1, number2):
        if number1 % i == 0 and number2 % i == 0:
            answer2 = i
        i += 1
    res = answer == str(answer2)
    return res, answer, answer2
