''' Game engine functions.
тут далее уже вся логика, цикл и тут используем
    логику описанную для каждой игры.'''

from random import randint
from brain_games.cli import welcome_user, user_answer

NUMBER_OF_ROUNDS = 3


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    flag = True
    while correct_answers < NUMBER_OF_ROUNDS:
        if user_answer == check:
            print('Correct!')
            flag = True
            correct_answers += 1
        else:
            flag = False
            break

    if flag:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{check}'\nLet's try again, {name}!")
    check, user_answer = game.get_question_and_answer()
