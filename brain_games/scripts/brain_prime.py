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
        k = False
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')        
        max_range = num // 2 + 2
        for delitel in range(2, max_range):
            if (num % delitel == 0 and delitel < num):
                k = False
                break
            else:
                k = True            

        if answer == 'yes' and k or answer == 'no' and not k:
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
