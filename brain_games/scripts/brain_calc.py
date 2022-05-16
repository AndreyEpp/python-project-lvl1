import prompt
import random


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    #print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    flag = True
    while i < 3:
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
        print('Question: {} {} {}'.format(num1, oper, num2))
        answer = prompt.string('Your answer: ')
        if int(answer) == check:
            print('Correct!')
            flag = True
            i += 1
        else:
            flag = False
            break

    if flag:
        #print(f'Congratulations, {name}!')
        print('Congratulations, {}!'.format(name))
    else:
        #print(f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!")
        print("'{}' is wrong answer ;(.\nLet's' try again, {}!".format(answer, name))

def main():
    brain_calc()


if __name__ == '__main__':
    main()
