'''Brain even game functions.'''

import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(0, 100)
    answer = 'no' if question % 2 else 'yes'
    return question, answer
