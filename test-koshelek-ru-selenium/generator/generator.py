import random
import string


class Generator:
    @staticmethod
    def generate_latin_string_digits(length: int = None) -> object:
        """
        Функция рандомной строки из букв верхнего, нижнего регистра на латинице и цифр
        :param length: длинна строки
        :return: рандомная строка
        """
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return rand_string

    @staticmethod
    def generate_latin_string(length: int = None) -> object:
        """
        Функция рандомной строки из букв верхнего, нижнего регистра на латинице
        :param length: длинна строки
        :return: рандомная строка
        """
        letters_and_digits = string.ascii_letters
        rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return rand_string

    @staticmethod
    def generate_latin_lowercase_string(length: int = None) -> object:
        """
        Функция рандомной строки из букв нижнего регистра на латинице
        :param length: длинна строки
        :return: рандомная строка
        """
        letters_and_digits = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return rand_string

    @staticmethod
    def generate_random_digits(length: int = None):
        """
        Функция рандомной строки из цифр
        :param length: длинна строки
        :return: рандомная строка
        """
        digits = string.digits
        rand_string = ''.join(random.choice(digits) for i in range(length))
        return rand_string

    @staticmethod
    def generate_cyrillic_string(length: int = None):
        """
        Функция рандомной строки из букв на кириллице
        :param length: длинна строки
        :return: рандомная строка
        """
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    @staticmethod
    def generate_cyrillic_string_digits(length):
        """
        Функция рандомной строки из букв верхнего и нижнего регистра на кириллице и цифр
        :param length: длинна строки
        :return: рандомная строка
        """
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    @staticmethod
    def generate_latin_string_digits_punctuation(length: int = None) -> object:
        """
        Функция рандомной строки из букв верхнего, нижнего регистра на латинице и цифр
        :param length: длинна строки
        :return: рандомная строка
        """
        letters_and_digits = string.ascii_letters + string.digits + string.punctuation
        rand_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return rand_string

    @staticmethod
    def generate_latin_cyrillic_string_digits_punctuation(length):
        """
        Функция рандомной строки из букв верхнего и нижнего регистра на кириллице и цифр
        :param length: длинна строки
        :return: рандомная строка
        """
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.ascii_letters + string.digits + string.punctuation
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string




