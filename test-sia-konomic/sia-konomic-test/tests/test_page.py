import pytest

from pom.registration_page import RegistrationPage

from settings import *


@pytest.mark.usefixtures('get_webdriver')
class TestPage:

    def test_check_all_empty_fields(self):
        """
        Тест - все поля пустые.
        :return: Проверка - "Поле не заполнено", чек бокс Пользовательское соглашение не активен
        """
        RegistrationPage(self.driver).click_submit_button()

        assert RegistrationPage(self.driver).username_form_checking_correctness == " Поле не заполнено "
        assert RegistrationPage(self.driver).email_form_checking_correctness == " Поле не заполнено "
        assert RegistrationPage(self.driver).password_form_checking_correctness == " Поле не заполнено "
        assert RegistrationPage(self.driver).checking_check_box_activity is False

    @pytest.mark.parametrize("username_parameter_entry_list", list_input_username)
    def test_field_username(self, username_parameter_entry_list: list):
        """
        Тест - проверки поля "Имя пользователя" - остальные поля заполнены валидными значениями
        FAILED - на тесты с пробелами до и после значения, т.е. пробелы в форму не вставляются.
        :param username_parameter_entry_list: Список проверок не валидных проверок
        :return: Проверка - "Поле не заполнено",
        " Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы "
        """
        RegistrationPage(self.driver).username_entry_field_list(username_parameter_entry_list)
        RegistrationPage(self.driver).email_entry_field(email_valid_value)
        RegistrationPage(self.driver).password_entry_field(password_valid_value)
        RegistrationPage(self.driver).click_submit_button_check_box()

        assert any(
            item in RegistrationPage(self.driver).username_form_checking_correctness for item in
            (" Поле не заполнено", " Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы "))

    @pytest.mark.parametrize("email_parameter_entry_list", list_input_email)
    def test_field_email(self, email_parameter_entry_list: list):
        """
        Тест - проверки поля "Электронная почта" - остальные поля заполнены валидными значениями
        FAILED - на тесты с пробелами до и после значения, т.е. пробелы в форму не вставляются.
        Выявлен баг электронная почта на кириллице.
        :param email_parameter_entry_list: Список проверок не валидных проверок
        :return: Проверка - "Формат e-mail: somebody@somewhere.ru", "Поле не заполнено"
        """
        RegistrationPage(self.driver).username_entry_field(username_valid_value)
        RegistrationPage(self.driver).email_entry_field_list(email_parameter_entry_list)
        RegistrationPage(self.driver).password_entry_field(password_valid_value)
        RegistrationPage(self.driver).click_submit_button_check_box()

        assert any(
            item in RegistrationPage(self.driver).email_form_checking_correctness for item in
            (" Формат e-mail: somebody@somewhere.ru ", " Поле не заполнено "))

    @pytest.mark.parametrize("password_parameter_entry_list", list_input_password)
    def test_field_password(self, password_parameter_entry_list: list):
        """
        Тест - проверки поля "Пароль" - остальные поля заполнены валидными значениями
        FAILED - на тесты с пробелами до и после значения, т.е. пробелы в форму не вставляются
        :param password_parameter_entry_list: Список проверок не валидных проверок
        :return: Проверка - "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры",
             "Пароль должен содержать минимум 8 символов", "Поле не заполнено"
        """
        RegistrationPage(self.driver).username_entry_field(username_valid_value)
        RegistrationPage(self.driver).email_entry_field(email_valid_value)
        RegistrationPage(self.driver).pasword_entry_field_list(password_parameter_entry_list)
        RegistrationPage(self.driver).click_submit_button_check_box()

        assert any(
            item in RegistrationPage(self.driver).password_form_checking_correctness for item in
            (" Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры ",
             " Пароль должен содержать минимум 8 символов ", " Поле не заполнено "))

    def test_referal_link(self):
        """
        Тест - проверки поля "Реферальный код" - остальные поля заполнены валидными значениями
        :return: Проверка - "Неверный формат ссылки", не активна кнопка "Долее"
        """
        RegistrationPage(self.driver).username_entry_field(username_valid_value)
        RegistrationPage(self.driver).email_entry_field(email_valid_value)
        RegistrationPage(self.driver).password_entry_field(password_valid_value)
        RegistrationPage(self.driver).referal_entry_field(link_referal)
        RegistrationPage(self.driver).click_check_box()

        assert RegistrationPage(self.driver).referal_form_checking_correctness == ' Неверный формат ссылки '
        assert RegistrationPage(self.driver).submit_button().is_enabled() is True
