''' Game engine functions.'''

import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.DESCRIPTION)
    game_rounds_count = 3
    for round_number in range(0, game_rounds_count):
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {user_name}!")            
            return
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
