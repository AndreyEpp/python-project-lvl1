'''Brain calc game functions.'''

import prompt
import random
import math
from brain_games.engine import run_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    check = math.gcd(num1, num2)
    print(f'Question: {num1} {num2}')
    user_answer = prompt.string('Your answer: ')
    return check, user_answer
