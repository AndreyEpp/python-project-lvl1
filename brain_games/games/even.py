'''Brain even game functions.'''

import prompt
import random
from brain_games.engine import run_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_question_and_answer():
    check = 'no'
    num = random.randint(0, 100)
    print('Question: {}'.format(num))
    answer = prompt.string('Your answer: ')
    if num % 2 == 0 and user_answer == 'yes' or num % 2 != 0 and user_answer == 'no':
        check = 'yes'
    else:
        check = 'no'
    return check, user_answer
    
    
