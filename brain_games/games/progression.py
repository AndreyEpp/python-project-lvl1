'''Brain progression game functions.'''

import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    list_a = []
    num_start = random.randint(1, 11)
    len_list = random.randint(5, 11)
    step = random.randint(1, 11)
    index_zameny = random.randint(0, len_list + 1)
    progression = list(range(num_start, (num_start + len_list * step), step))
    check, progression[index_zameny] = progression[index_zameny], '..'
    progression = " ".join(map(str,progression))
    return check, user_answer
