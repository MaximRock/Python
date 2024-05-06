from generator.generator import Generator
from pom.registration_page import RegistrationPage


class Data:

    required_fields = [
        ''
    ]

    username_list = [
        # '',
        Generator.generate_cyrillic_string(1),
        Generator.generate_cyrillic_string(33),
        Generator.generate_cyrillic_string_digits(6),
        Generator.generate_cyrillic_string(1000),
        Generator.generate_cyrillic_string_digits(1000),
        Generator.generate_latin_cyrillic_string_digits_punctuation(15),
        Generator.generate_latin_string(1),
        Generator.generate_random_digits(1),
        Generator.generate_latin_string_digits(5),
        Generator.generate_latin_string_digits(33),
        Generator.generate_latin_string(1000),
        Generator.generate_latin_string_digits(1000),
        Generator.generate_latin_string_digits_punctuation(15),
        Generator.generate_random_digits(25),
    ]

    email_list = [
        # '',
        'тестрок75@gmail.com',
        Generator.generate_cyrillic_string(1000),
        Generator.generate_cyrillic_string_digits(1000),
        Generator.generate_latin_cyrillic_string_digits_punctuation(15),
        'testrock75gmail.com',
        'testrock75@gmailcom',
        'testrock75@gmail',
        '@gmail.com',
        Generator.generate_latin_string(1000),
        Generator.generate_latin_string_digits(1000),
        Generator.generate_latin_string_digits_punctuation(15),
        Generator.generate_random_digits(25),
        Generator.generate_random_digits(25)
    ]

    password_list = [
        # '',
        Generator.generate_cyrillic_string(1),
        Generator.generate_cyrillic_string_digits(7),
        Generator.generate_cyrillic_string_digits(65),
        Generator.generate_cyrillic_string(1000),
        Generator.generate_cyrillic_string_digits(1000),
        Generator.generate_latin_cyrillic_string_digits_punctuation(100),
        Generator.generate_latin_string(1),
        Generator.generate_random_digits(1),
        Generator.generate_latin_string_digits(7),
        Generator.generate_latin_string_digits(65),
        Generator.generate_latin_string(1000),
        Generator.generate_latin_string_digits(1000),
        Generator.generate_random_digits(25)
    ]

    referral_list = [
        Generator.generate_cyrillic_string(1),
        Generator.generate_cyrillic_string(1000),
        Generator.generate_cyrillic_string_digits(1000),
        Generator.generate_latin_cyrillic_string_digits_punctuation(100),
        Generator.generate_latin_string(1),
        Generator.generate_random_digits(1),
        Generator.generate_latin_string(1000),
        Generator.generate_latin_string_digits(1000),
        Generator.generate_random_digits(100)
    ]

    icon_russian_text_list = [
        Generator.generate_cyrillic_string(1),
        Generator.generate_cyrillic_string(10),
        Generator.generate_cyrillic_string_digits(10),
        Generator.generate_latin_cyrillic_string_digits_punctuation(20)
    ]

    russian_text_list = [
        'cyrillic_string-1.png',
        'cyrillic_string-10.png',
        'cyrillic_string_digits-10.png',
        'latin_cyrillic_string_digits_punctuation-20.png'
    ]

    text_with_space = [
        f'      {Generator.generate_latin_string(10)}',
        f'{Generator.generate_latin_string(8)}       ',
        f'{Generator.generate_latin_string(4)}    {Generator.generate_latin_string(4)}'
    ]

    path_screenshot_password_ru_icon = "screenshot/password_field_ru_icon/"

    email_correctness = 'testrock75@gmail.com'
    username_correctness = Generator.generate_latin_lowercase_string(20)
    password_correctness = Generator.generate_latin_string_digits(20)


