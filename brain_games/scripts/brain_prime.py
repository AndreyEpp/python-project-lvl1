import prompt
import random
import math

def brain_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')
    flag = True
    i = 0
    while i < 3:
        num = random.randint(0,100)
        k = 0
        print(f'Question: {num}')
        for delitel in range(2, num // 2 + 1):
            if (num % delitel == 0):
                k = k + 1
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and k == 0 or answer == 'no' and k != 0:
            print(f'Correct!')
            flag = True
            i += 1
        else:
            flag = False
            break

    if flag == True:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(.\nLet's try again, {name}!")

def main():
    brain_prime()


if __name__== '__main__':
    main()
