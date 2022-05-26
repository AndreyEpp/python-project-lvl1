'''Brain even game functions.'''

import prompt
import random
from brain_games.engine import run_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_question_and_answer():
    yes_no = 'no'
    while i < 3:
        num = random.randint(0, 100)
        print('Question: {}'.format(num))
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print('Correct!')
            i = i + 1
            flag = True
        else:
            if answer == 'no':
                yes_no = 'yes'
            else:
                yes_no = 'no'
            flag = False
            break
    if flag:
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'\n"
              "Let's try again, {}!".format(answer, yes_no, name))


def main():
    brain_even()


if __name__ == '__main__':
    main()
