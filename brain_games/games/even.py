'''Brain even game functions.'''

import prompt
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    check = 'no'
    num = random.randint(0, 100)
    print(f'Question: {num}')
    user_answer = prompt.string('Your answer: ')
    if num % 2 == 0:
        check = 'yes'
    else:
        check = 'no'
    return check, user_answer
