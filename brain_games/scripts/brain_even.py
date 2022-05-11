import prompt
import random

def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    num = random.randint(0, 100)
    print(f'Question: {num}')
    answer = prompt.string(f'Your answer: ')
    i = 0
    flag = True
    yes_no = 'no'
    while i < 2:
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print(f'Correct!')
            i = i + 1
            flag = True
            num = random.randint(0, 100)
            print(f'Question: {num}')
            answer = prompt.string(f'Your answer: ')
        else:
            if answer == 'no':
                yes_no = 'yes'
            else:
                yes_no  = 'no'
            flag = False
            break    
    if flag == True:
        print(f'Correct!\nCongratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{yes_no}'.\nLet's try again, {name}!")
            


def main():
    brain_even()


if __name__ == '__main__':
    main()
