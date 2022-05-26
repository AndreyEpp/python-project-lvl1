'''Brain prime game functions.'''

import prompt
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    num = random.randint(0, 100)
    check = 'no'
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    max_range = num // 2 + 2
    for delitel in range(2, max_range):
        if (num % delitel == 0 and delitel < num):
            check = 'no'
            break
        else:
            check = 'yes'
    return check, user_answer
