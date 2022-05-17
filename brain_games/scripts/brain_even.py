import prompt
import random


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    flag = True
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
