'''User input'''

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer
