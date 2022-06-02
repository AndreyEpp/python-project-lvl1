''' Game engine functions.'''

from brain_games.cli import welcome_user
import prompt

NUMBER_OF_ROUNDS = 3


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    flag = True
    while correct_answers < NUMBER_OF_ROUNDS:
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            flag = True
            correct_answers += 1
        else:
            flag = False
            break

    if flag:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{answer}'\n"
              f"Let's try again, {name}!")
