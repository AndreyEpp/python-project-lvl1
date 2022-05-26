'''Brain progression game functions.'''

import prompt
import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    list_a = []
    num_start = random.randint(1, 10)
    len_list = random.randint(5, 10)
    index_zameny = random.randint(0, len_list)
    s = ''
    for num in range(0, len_list + 1):
        list_a.append(num_start * (num + 1))
        if index_zameny == num:
            s = s + '.. '
        else:
            s = s + str(num_start * (num + 1)) + ' '
    check = list_a[index_zameny]
    print(f'Question: {s}')
    user_answer = int(prompt.string('Your answer: '))
    return check, user_answer
