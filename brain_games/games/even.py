'''Brain even game functions.'''

import prompt
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(0, 100)
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    check = 'no' if question % 2 else 'yes'
    return check, user_answer
