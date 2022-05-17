import prompt
import random
from brain_games.cli import welcome_user


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag = True
    i = 0
    while i < 3:
        num = random.randint(0, 100)
        k = 0
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if num > 2:
            max_range = num // 2 + 1
            for delitel in range(2, max_range):
                if (num % delitel == 0):
                    k = k + 1
        else:
            if num != 2:
                k = 1

        if answer == 'yes' and k == 0 or answer == 'no' and k != 0:
            print('Correct!')
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
    brain_prime()


if __name__ == '__main__':
    main()
