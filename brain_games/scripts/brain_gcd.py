import prompt
import random
import math


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    flag = True
    while i < 3:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        nod = math.gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        answer = prompt.string('Your answer: ')
        if int(answer) == nod:
            print(f'Correct!')
            flag = True
            i += 1
        else:
            flag = False
            break

    if flag:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
