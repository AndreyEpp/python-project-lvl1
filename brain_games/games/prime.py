'''Brain prime game functions.'''

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num > 2 and not num % 2:
        return False

    div = 3
    while div <= num // 2:
        if not num % div:
            return False
        div += 2
    return True


def get_question_and_answer():
    num = random.randint(1, 100)
    question = f'{num}'
    answer = 'yes' if is_prime(num) else 'no'
    return question, answer
