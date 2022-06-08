''' Game engine functions.'''

from brain_games.cli import welcome_user
import prompt


def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    game_rounds_count = 3
    for round_number in range(0, game_rounds_count):
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            flag = True
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {name}!")
            flag = False
            break

    if flag:
        print(f'Congratulations, {name}!')
