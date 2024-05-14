import pytest
from allpairspy import AllPairs
from pom.registration_page import RegistrationPage
from data.data import Data
import allure
from allure_commons.types import AttachmentType
import time


@pytest.mark.usefixtures('get_webdriver')
@pytest.mark.all_tests
@allure.suite("RegistrationPage")
class TestPage:

    @pytest.mark.checkbox
    @allure.feature("fields_empty")
    def test_all_fields_empty(self):
        """
        Check_box - Пользовательское соглашение
        Тест - все поля пустые, нажать кнопку "Далее"
        :return: Все поля пустые, check_box - Пользовательское соглашение не активен
        """
        registration_page = RegistrationPage(self.driver)
        registration_page.click_submit_button()

        assert any(item in registration_page.username_form_checking_correctness for item in " Поле не заполнено")
        assert any(item in registration_page.email_form_checking_correctness for item in " Поле не заполнено ")
        assert any(item in registration_page.password_form_checking_correctness for item in " Поле не заполнено ")

        assert registration_page.user_agreement_check_box_is_enabled

    @pytest.mark.checkbox
    @allure.feature("fields_empty")
    def test_checkbox_is_not(self):
        """
        Check_box - Пользовательское соглашение
        Тест - все поля заполнены валидными парамерами, нажать кнопку "Далее"
        :return: Все поля заполнены, check_box - Пользовательское соглашение не активен
        """
        registration_page = RegistrationPage(self.driver)
        registration_page.username_entry_field_list(Data.username_correctness)
        registration_page.email_entry_field_list(Data.email_correctness)
        registration_page.password_entry_field_list(Data.password_correctness)
        registration_page.click_submit_button()

        assert registration_page.user_agreement_check_box_is_enabled

    @pytest.mark.parametrize(["username", "email", "password", "referral"], [
        values for values in AllPairs([
            Data.username_list,
            Data.email_list,
            Data.password_list,
            Data.referral_list,
        ])
    ])
    @pytest.mark.pairs
    @allure.feature("pairs_fields")
    def test_pairs_fields(self, username, email, password, referral):
        """
        Тест - с применением Pairwise полей "Имя пользователя",
            "Электронная почта", "Пароль", "Реферальный код"
        :param username: с генерированные данные из списка username_list
        :param email: с генерированные данные из списка email_list
        :param password: с генерированные данные из списка password_list
        :param referral: с генерированные данные из списка referral_list
        :return: Негативное тестирование всех полей
        """
        registration_page = RegistrationPage(self.driver)
        registration_page.username_entry_field_list(username)
        registration_page.email_entry_field_list(email)
        registration_page.password_entry_field_list(password)
        registration_page.referal_entry_field(referral)
        # registration_page.click_submit_button_check_box()

        assert any(
            item in registration_page.username_form_checking_correctness for item in
            (" Поле не заполнено", " Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы "))
        assert any(
            item in registration_page.email_form_checking_correctness for item in
            (" Формат e-mail: username@test.ru ", " Поле не заполнено "))
        assert any(
            item in registration_page.password_form_checking_correctness for item in
            (" Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры ",
             " Пароль должен содержать минимум 8 символов ", " Поле не заполнено "))
        assert any(
            item in registration_page.referal_form_checking_correctness for item in
            "  Неверный формат ссылки  ")

    @pytest.mark.parametrize('username', Data.username_list)
    @pytest.mark.username
    @allure.feature("username_pop_up")
    @allure.story("username_is_invalid")
    def test_username_is_invalid(self, username):
        """
        Тест - проверки всплывающего окна 'Имя пользователя недействительно'
        :param username: List Data.username_list
        :return: Сравниваем полученный текст.
        """
        registration_page = RegistrationPage(self.driver)
        registration_page.username_entry_field_list(username)
        registration_page.email_entry_field_list(Data.email_correctness)
        registration_page.password_entry_field_list(Data.password_correctness)

        with allure.step("Получаем текст - 'Имя пользователя недействительно'"):
            assert registration_page.username_pop_up_text == 'Имя пользователя недействительно'

    @pytest.mark.parametrize("text_space", Data.text_with_space)
    @pytest.mark.space
    @allure.feature("field_space")
    @allure.story("username_field")
    def test_username_field_space(self, text_space):
        """
        Поле - Username
        Тест - проверки ввода данных с использованием пробелов
        :param text_space: List Data.text_with_space
        :return: Проверка на не равенство введенных данных
        """
        registration_page = RegistrationPage(self.driver)
        with allure.step("Сравниваем введенные параметры и полученные параметры"):
            assert registration_page.username_entry_field_list(
                text_space) != registration_page.username_text_from_field()

    @pytest.mark.parametrize("text_space", Data.text_with_space)
    @pytest.mark.space
    @allure.feature("field_space")
    @allure.story("email_field")
    def test_email_field_space(self, text_space):
        """
        Поле - Email
        Тест - проверки ввода данных с использованием пробелов
        :param text_space: List Data.text_with_space
        :return: Проверка на не равенство введенных данных
        """
        registration_page = RegistrationPage(self.driver)
        with (allure.step("Сравниваем введенные параметры и полученные параметры")):
            assert registration_page.email_entry_field_list(text_space) != registration_page.email_text_from_field()

    @pytest.mark.parametrize("text_space", Data.text_with_space)
    @pytest.mark.space
    @allure.feature("field_space")
    @allure.story("password_field")
    def test_password_field_space(self, text_space):
        """
        Поле - Password
        Тест - проверки ввода данных с использованием пробелов
        :param text_space: List Data.text_with_space
        :return: Проверка на не равенство введенных данных
        """
        registration_page = RegistrationPage(self.driver)
        with (allure.step("Сравниваем введенные параметры и полученные параметры")):
            assert registration_page.password_entry_field_list(
                text_space) != registration_page.password_text_from_field()

    @pytest.mark.parametrize("text_space", Data.text_with_space)
    @pytest.mark.space
    @allure.feature("field_space")
    @allure.story("referal_field")
    def test_referal_field_space(self, text_space):
        """
        Поле - Referal
        Тест - проверки ввода данных с использованием пробелов
        :param text_space: List Data.text_with_space
        :return: Проверка на не равенство введенных данных
        """
        registration_page = RegistrationPage(self.driver)
        with (allure.step("Сравниваем введенные параметры и полученные параметры")):
            assert registration_page.referal_entry_field(text_space) != registration_page.referal_text_from_field()

    @pytest.mark.screenshot
    @allure.feature('screenshot')
    def test_password_icon_russian_text(self):
        """
        Тест - проверка появления иконки "RU" при вводе пароля на русском языке,
            а так же видимости вводимого пароля.
        :return: Создание скриншотов
        """
        registration_page = RegistrationPage(self.driver)
        registration_page.username_entry_field_list(Data.username_correctness)
        registration_page.email_entry_field_list(Data.email_correctness)
        registration_page.password_visibility_icon_click()
        for index in range(len(Data.icon_russian_text_list)):
            registration_page.password_entry_field_list(Data.icon_russian_text_list[index])
            registration_page.screenshot(f"{Data.path_screenshot_password_ru_icon}{Data.russian_text_list[index]}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'{Data.russian_text_list[index]}',
                attachment_type=AttachmentType.PNG
            )

            assert any(
                item in registration_page.password_entry_field_ru for item in "RU"
            )
