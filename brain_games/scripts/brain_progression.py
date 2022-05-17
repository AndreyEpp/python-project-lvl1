import prompt
import random


def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    flag = True
    while i < 3:
        list_a = []
        num_start = random.randint(1, 10)
        len_list = random.randint(5, 10)
        index_zameny = random.randint(0, len_list)
        s = ''
        for num in range(0, len_list + 1):
            list_a.append(num_start * (num + 1))
            if index_zameny == num:
                s = s + '.. '
            else:
                s = s + str(num_start * (num + 1)) + ' '
        value_zameny = list_a[index_zameny]
        print(f'Question: {s}')
        answer = prompt.string('Your answer: ')
        if int(answer) == value_zameny:
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
    brain_progression()


if __name__ == '__main__':
    main()
