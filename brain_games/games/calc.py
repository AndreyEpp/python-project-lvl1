'''тут как то создаем пару вопрос и ответ.'''

import prompt
import random
from brain_games.engine import run_game


DESCRIPTION = 'What is the result of the expression?'

def get_question_and_answer():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    foo = ['+', '-', '*']
    oper = random.choice(foo)
    if oper == '+':
        check = num1 + num2
    elif oper == '-':
        check = num1 - num2
    else:
        check = num1 * num2
    print(f'Question: {num1} {oper} {num2}')
    user_answer = prompt.string('Your answer: ')
    return question, user_answer


# def brain_calc():
#     print('Welcome to the Brain Games!')
#     name = prompt.string('May I have your name? ')
#     print('Hello, {}!'.format(name))
#     print('What is the result of the expression?')
#     i = 0
#     flag = True
#     while i < 3:
#         num1 = random.randint(0, 100)
#         num2 = random.randint(0, 100)
#         foo = ['+', '-', '*']
#         oper = random.choice(foo)
#         if oper == '+':
#             check = num1 + num2
#         elif oper == '-':
#             check = num1 - num2
#         else:
#             check = num1 * num2
#         print('Question: {} {} {}'.format(num1, oper, num2))
#         answer = prompt.string('Your answer: ')
#         if int(answer) == check:
#             print('Correct!')
#             flag = True
#             i += 1
#         else:
#             flag = False
#             break

#     if flag:
#         print('Congratulations, {}!'.format(name))
#     else:
#         print("'{}' is wrong answer ;(.\n"
#               "Let's try again, {}!".format(answer, name))


# def main():
#     brain_calc()


# if __name__ == '__main__':
#     main()
