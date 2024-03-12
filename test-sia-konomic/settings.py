import random
import string


def generate_alphanum_random_string_latin(length):
    '''
    Функция рандомной строки из букв верхнего и нижнего регистра на латинице и цифр
    :param length: длинна строки
    :return: рандомная строка
    '''
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
    return rand_string


def generate_random_string_digits(length):
    '''
    Функция рандомной строки из цифр
    :param length: длинна строки
    :return: рандомная строка
    '''
    digits = string.digits
    rand_string = ''.join(random.choice(digits) for i in range(length))
    return rand_string


def generate_random_string_cyrillic(length):
    '''
    Функция рандомной строки из букв на кириллице
    :param length: длинна строки
    :return: рандомная строка
    '''
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_string_mixed(length):
    '''
    Функция рандомной строки из букв верхнего и нижнего регистра на кириллице и цифр
    :param length: длинна строки
    :return: рандомная строка
    '''
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_string_spec_characters(length):
    """
    Функция рандомной строки из букв верхнего и нижнего регистра на латинице, цифр, спец. символов
    :param length: длинна строки
    :return: рандомная строка
    """
    letters = string.punctuation + string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


list_input_username = ['', 'a', '1', 'п', generate_alphanum_random_string_latin(5),
                       generate_alphanum_random_string_latin(33),
                       generate_random_string_cyrillic(6),
                       generate_random_string_cyrillic(1000),
                       generate_alphanum_random_string_latin(1000),
                       generate_random_string_mixed(1000),
                       generate_random_string_spec_characters(10),
                       generate_random_string_digits(30),
                       f'    {generate_alphanum_random_string_latin(10)}',
                       f'{generate_alphanum_random_string_latin(10)}    '
                       ]

list_input_email = ['', 'testrock75gmail.com', 'testrock75@gmail com', 'testrock75@gmail', '@gmail.com',
                    'максим@gmail.com', '1',
                    generate_random_string_cyrillic(1000),
                    generate_alphanum_random_string_latin(1000),
                    generate_random_string_mixed(1000),
                    generate_random_string_spec_characters(10),
                    generate_random_string_digits(30),
                    '    testrock75@gmail.com',
                    'testrock75@gmail.com    '
                    ]

list_input_password = ['', 'a', '1', 'п',
                       generate_random_string_spec_characters(7),
                       generate_random_string_spec_characters(65),
                       generate_random_string_cyrillic(6),
                       generate_random_string_cyrillic(1000),
                       generate_alphanum_random_string_latin(1000),
                       generate_random_string_mixed(1000),
                       generate_random_string_digits(64),
                       f'    {generate_alphanum_random_string_latin(10)}',
                       f'{generate_alphanum_random_string_latin(10)}    '
                       ]

username_valid_value = 'max_rock_test'
email_valid_value = 'testrock75@gmail.com'
password_valid_value = generate_random_string_spec_characters(20)
link_referal = 'https://test'
