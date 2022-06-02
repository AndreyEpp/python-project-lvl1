'''Brain progression game functions.'''

import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    list_a = []
    num_start = random.randint(1, 10)
    len_list = random.randint(5, 10)
    step = random.randint(1, 10)
    index_zameny = random.randint(0, len_list)
    progression = list(range(num_start, (num_start + len_list * step), step))
    answer, progression[index_zameny] = progression[index_zameny], '..'
    question = " ".join(map(str,progression))
    return question, str(answer)
