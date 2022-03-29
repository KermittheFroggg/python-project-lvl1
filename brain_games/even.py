import prompt
import random
from brain_games.cli import welcome_user


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        number = random.randint(1, 100000000000)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        var1 = answer == 'yes' and number % 2 == 0
        var2 = answer == 'no' and number % 2 != 0
        if var1 or var2:
            print('Correct!')
            if i == 3:
                print('Congratulations, ' + name + '!')
            i += 1
        else:
            text1 = ' is wrong answer ;(. Correct answer was '
            text2 = ". \nLet's try again, "
            if answer == 'yes':
                print('yes' + text1 + 'no' + text2 + name + "!")
            elif answer == 'no':
                print('no' + text1 + 'yes' + text2 + name + "!")
            else:
                print(name + ", ты напечатал какую-то ерунду!")
            break
