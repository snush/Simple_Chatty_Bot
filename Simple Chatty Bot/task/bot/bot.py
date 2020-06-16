def greet(bot_name, birth_year):
    print('Hello! My name is {}.'.format(bot_name))
    print('I was created in {}.'.format(birth_year))


def remind_name():
    name = input('Please, remind me your name.\n')
    print('What a great name you have, {}!'.format(name))


def guess_age():
    print('Let me guess your age.\n'
          'Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {}; that's a good time to start programming!".format(age))


def count():
    number = int(input('Now I will prove to you that I can count to any number you want.\n'))
    for i in range(number + 1):
        print('{}!'.format(i))


def test():
    print("Let's test your programming knowledge.\n"
          "Why do we use methods?\n"
          "1. To repeat a statement multiple times.\n"
          "2. To decompose a program into several small subroutines.\n"
          "3. To determine the execution time of a program.\n"
          "4. To interrupt the execution of a program.")

    while int(input()) != 2:
        print("Please, try again.")

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Sveta', '2020')
remind_name()
guess_age()
count()
test()
end()