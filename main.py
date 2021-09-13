import random
import string
import os
from colorama import Fore, Style


settings = {

    'lower': True,
    'upper': True,
    'number': True,
    'symbol': True,
    'space': False,
    'length': 8

}


def clear_screen():
    os.system('cls')


def welcome_func():
    print(f'\n*************************\
            ({Fore.BLUE}Random Password Generator{Style.RESET_ALL})\
            *************************\n')
    print('Developer:   (Mahdi Malekifard)\n')
    print('Email:   (mmf1374py@gmail.com)\n')
    print('*'*60 + '\n')


PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30


def get_user_input_length(_, default, pw_min_len=PASSWORD_MIN_LENGTH,
                          pw_max_len=PASSWORD_MAX_LENGTH):

    while True:

        user_input = input('Enter password length. '
                           f' (Default is {default}) (default: enter):  ')

        if user_input == '':
            return default

        if user_input.isdigit():
            user_pass_length = int(user_input)

            if pw_min_len <= user_pass_length <= pw_max_len:
                return user_pass_length

            print('Invalid input')
            print(
                f'You should enter a number between {pw_min_len} and {pw_max_len}')

        else:
            print('Invalid input. You should enter a number!')

        print('Please try again.')


def get_yes_no_for_settings(option, default):

    while True:

        user_input = input(f'Include {option} (Default: {default}) '
                           '(yes: y, no: n, default: enter): ')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print('Invalid input. Please try again.')


def user_change_settings(settings):

    for option, default in settings.items():

        if option != 'length':
            user_choice = get_yes_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_length_choice = get_user_input_length(option, default)
            settings[option] = user_length_choice


def ask_if_to_change_settings(settings):

    while True:

        user_answer = input('Would you like to change the default settings?'
                            ' (y: yes, n: no, enter: yes)  ')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print()
                print(
                    f'{Fore.LIGHTMAGENTA_EX}settings{Style.RESET_ALL}:\
                     -----------------')
                user_change_settings(settings)
            break

        else:
            print('Invalid input!')
            print('Please try again.')


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_number():
    return random.choice('0123456789')


def get_random_symbol():
    return random.choice(string.punctuation)


def generate_random_char(choices):

    choice = random.choice(choices)

    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'number':
        return get_random_number()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'space':
        return ' '


def password_generator(settings):
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], [
                   'lower', 'upper', 'number', 'symbol', 'space']))

    for _ in range(password_length):
        final_password += generate_random_char(choices)

    with open('PassFile.txt', 'a') as f:
        f.write(f'{final_password}\n')

    return 'go to -PassFile.txt-'


def ask_user_to_generate_another_password():

    while True:
        user_answer = input('Regenerate?  (y: yes, n: no, enter: yes)  ')

        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True

        else:
            print('Invalid input. (Choose from y: yes, n: no, enter: yes)')
            print('Please try again.')


def password_generator_loop(settings):

    while True:
        print('-'*20)
        print(
            f'{Fore.GREEN}Generated Password{Style.RESET_ALL}:\
            {password_generator(settings)}')

        if ask_user_to_generate_another_password() == False:
            break


def run():

    clear_screen()
    welcome_func()
    ask_if_to_change_settings(settings)
    password_generator_loop(settings)


if __name__ == "__main__":
    run()
