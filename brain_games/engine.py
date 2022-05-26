''' Game engine functions.'''

from random import randint
from brain_games.cli import get_user_answer, get_user_name

NUMBER_OF_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    i = 0
    flag = True
    тут далее уже вся логика, цикл и тут используем
    логику описанную для каждой игры.
    print(game.DESCRIPTION)
    question, correct_answer = game.get_question_and_answer()
