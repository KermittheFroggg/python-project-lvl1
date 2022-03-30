import prompt
import random


def prime():
    number = random.randint(1, 100)
    print('Question: ' + str(number))
    answer = prompt.string('Your answer: ')
    i = 2
    calc = 0
    answer2 = 'yes'
    while i < number:
        if number % i == 0:
            calc += 1
        i += 1
    if calc >= 1:
        answer2 = 'no'
    res = answer == answer2
    return res, answer, answer2
