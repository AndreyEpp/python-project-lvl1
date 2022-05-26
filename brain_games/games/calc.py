'''Brain calc game functions.'''

import prompt
import random


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    foo = ['+', '-', '*']
    oper = random.choice(foo)
    if oper == '+':
        check = num1 + num2
    elif oper == '-':
        check = num1 - num2
    else:
        check = num1 * num2
    print(f'Question: {num1} {oper} {num2}')
    user_answer = int(prompt.string('Your answer: '))
    return check, user_answer
