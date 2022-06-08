'''Brain calc game functions.'''

import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operations = {
   '+': operator.add,
   '-': operator.sub,
   '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))
    answer = str(operations[operation](num1, num2))
    question = f'{num1} {oper} {num2}'
    return question, answer
