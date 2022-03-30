import prompt
import random


def progression():
    lenght = random.randint(6, 10)
    index_miss = random.randint(1, lenght)
    x = 1
    progression = ''
    next_number = random.randint(1, 100)
    step = random.randint(1, 10)
    while x <= lenght:
        if x == index_miss:
            answer2 = next_number
            progression = progression + '.. '
        else:
            progression = progression + str(next_number) + ' '
        next_number = next_number + step
        x += 1
    print('Question: ' + progression)
    answer = prompt.string('Your answer: ')
    res = answer == str(answer2)
    return res, answer, answer2
