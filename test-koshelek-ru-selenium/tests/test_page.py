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
            assert registration_page.username_entry_field_list(text_space) != registration_page.username_text_from_field()

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
            assert registration_page.password_entry_field_list(text_space) != registration_page.password_text_from_field()

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
            registration_page.password_save_screenshot(
                f"{Data.path_screenshot_password_ru_icon}{Data.russian_text_list[index]}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f'{Data.russian_text_list[index]}',
                attachment_type=AttachmentType.PNG
            )

            assert any(
                item in registration_page.password_entry_field_ru for item in "RU"
            )

    # # @pytest.mark.parametrize("russian_text", icon_russian_text_list)
    # def test_test(self):
    #     registration_page = RegistrationPage(self.driver)
    #     registration_page.username_entry_field_list(username_correctness)
    #     registration_page.email_entry_field_list(email_correctness)
    #     registration_page.password_visibility_icon_click()
    #     for index in range(4):
    #         registration_page.password_entry_field_list(icon_russian_text_list[index])
    #         registration_page.password_save_screenshot(f"{path_screenshot_username}{russian_text_list[index]}")
    #         # time.sleep(2)

    # registration_page.password_entry_field_list(russian_text)
    # registration_page.screenshot(f'{path_screenshot_username}{russian_text_list}')
    #
    #
    #
    # @pytest.mark.parametrize("username_parameter_entry_list", list_input_username)
    # def test_field_username(self, username_parameter_entry_list: list):
    #     """
    #     Тест - проверки поля "Имя пользователя" - остальные поля заполнены валидными значениями
    #     FAILED - на тесты с пробелами до и после значения, т.е. пробелы в форму не вставляются.
    #     :param username_parameter_entry_list: Список проверок не валидных проверок
    #     :return: Проверка - "Поле не заполнено",
    #     " Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы "
    #     """
    #     RegistrationPage(self.driver).username_entry_field_list(username_parameter_entry_list)
    #     RegistrationPage(self.driver).email_entry_field(email_valid_value)
    #     RegistrationPage(self.driver).password_entry_field(password_valid_value)
    #     RegistrationPage(self.driver).click_submit_button_check_box()
    #
    #     assert any(
    #         item in RegistrationPage(self.driver).username_form_checking_correctness for item in
    #         (" Поле не заполнено", " Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы "))
    #
    # @pytest.mark.parametrize("email_parameter_entry_list", list_input_email)
    # def test_field_email(self, email_parameter_entry_list: list):
    #     """
    #     Тест - проверки поля "Электронная почта" - остальные поля заполнены валидными значениями
    #     FAILED - на тесты с пробелами до и после значения, т.е. пробелы в форму не вставляются.
    #     Выявлен баг электронная почта на кириллице.
    #     :param email_parameter_entry_list: Список проверок не валидных проверок
    #     :return: Проверка - "Формат e-mail: somebody@somewhere.ru", "Поле не заполнено"
    #     """
    #     RegistrationPage(self.driver).username_entry_field(username_valid_value)
    #     RegistrationPage(self.driver).email_entry_field_list(email_parameter_entry_list)
    #     RegistrationPage(self.driver).password_entry_field(password_valid_value)
    #     RegistrationPage(self.driver).click_submit_button_check_box()
    #
    #     assert any(
    #         item in RegistrationPage(self.driver).email_form_checking_correctness for item in
    #         (" Формат e-mail: username@test.ru ", " Поле не заполнено "))
    #
    # def test_check_all_empty_fields(self):
    #
    #     """
    #     Тест - все поля пустые.
    #     :return: Проверка - "Поле не заполнено", чек бокс Пользовательское соглашение не активен
    #     """
    #     RegistrationPage(self.driver).click_submit_button()
    #
    #     assert RegistrationPage(self.driver).username_form_checking_correctness == " Поле не заполнено "
    #     assert RegistrationPage(self.driver).email_form_checking_correctness == " Поле не заполнено "
    #     assert RegistrationPage(self.driver).password_form_checking_correctness == " Поле не заполнено "
    #     assert RegistrationPage(self.driver).checking_check_box_activity is False
    #
    # @pytest.mark.parametrize("password_parameter_entry_list", list_input_password)
    # def test_field_password(self, password_parameter_entry_list: list):
    #     """
    #     Тест - проверки поля "Пароль" - остальные поля заполнены валидными значениями
    #     :param password_parameter_entry_list: Список проверок не валидных проверок
    #     :return: Проверка - "Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры",
    #          "Пароль должен содержать минимум 8 символов", "Поле не заполнено"
    #     """
    #     RegistrationPage(self.driver).username_entry_field(username_valid_value)
    #     RegistrationPage(self.driver).email_entry_field(email_valid_value)
    #     RegistrationPage(self.driver).password_entry_field_list(password_parameter_entry_list)
    #     RegistrationPage(self.driver).click_submit_button_check_box()
    #
    #     assert any(
    #         item in RegistrationPage(self.driver).password_form_checking_correctness for item in
    #         (" Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры ",
    #          " Пароль должен содержать минимум 8 символов ", " Поле не заполнено "))
    #
    # @pytest.mark.parametrize("password_parameter_entry_list_ru", list_input_password_cyrillic)
    # def test_field_password_ru(self, password_parameter_entry_list_ru):
    #     """
    #
    #     :param password_parameter_entry_list_ru:
    #     :return:
    #     """
    #     RegistrationPage(self.driver).username_entry_field(username_valid_value)
    #     RegistrationPage(self.driver).email_entry_field(email_valid_value)
    #     RegistrationPage(self.driver).password_entry_field_list(password_parameter_entry_list_ru)
    #     RegistrationPage(self.driver).password_visibility_icon_click()
    #     RegistrationPage(self.driver).click_submit_button_check_box()
    #
    #     time.sleep(3)
    #
    #     assert RegistrationPage(self.driver).password_entry_field_ru().is_enabled() is True
    #     assert RegistrationPage(self.driver).password_visibility_icon_activ().is_selected() is True
    #
    # def test_referal_link(self):
    #     """
    #     Тест - проверки поля "Реферальный код" - остальные поля заполнены валидными значениями
    #     :return: Проверка - "Неверный формат ссылки", не активна кнопка "Долее"
    #     """
    #     RegistrationPage(self.driver).username_entry_field(username_valid_value)
    #     RegistrationPage(self.driver).email_entry_field(email_valid_value)
    #     RegistrationPage(self.driver).password_entry_field(password_valid_value)
    #     RegistrationPage(self.driver).referal_entry_field(link_referal)
    #     RegistrationPage(self.driver).click_check_box()
    #
    #     assert RegistrationPage(self.driver).referal_form_checking_correctness == ' Неверный формат ссылки '
    #     assert RegistrationPage(self.driver).submit_button().is_enabled() is True
    #
