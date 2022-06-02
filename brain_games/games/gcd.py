'''Brain gcd game functions.'''

import prompt
import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)
    return check, user_answer
