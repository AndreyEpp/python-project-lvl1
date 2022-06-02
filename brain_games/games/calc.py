'''Brain calc game functions.'''

import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    foo = ['+', '-', '*']
    oper = random.choice(foo)
    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f'{num1} {oper} {num2}'
    return question, str(answer)
