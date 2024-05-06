import allure
import os
from selenium.webdriver.remote.webelement import WebElement
from base.base import BasePage
from allure_commons.types import AttachmentType


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__nav: str = '//span[contains(text(),"Зарегистрироваться")]'
        self.__shadow_host: str = 'div.remoteComponent'
        self.__username_checking_correctness: str = '[data-wi=user-name] [data-wi=message] span.k-text'
        self.__email_checking_correctness: str = '[data-wi=identificator] [data-wi=message] span.k-text'
        self.__password_checking_correctness: str = '[data-wi=password] [data-wi=error] span.k-text'
        self.__password_checking_correctness_ru: str = \
            '[data-wi=password] [data-pw=auth-widget-password-input-append] span.k-text'
        self.__password_visibility_icon: str = '[data-wi=password] [type=button]'
        self.__password_visibility_icon_click: str = '[data-wi=password] [name=AUTH.preview-open]'
        self.__submit_button: str = '[data-wi=submit-button] span.v-btn__content'
        self.__check_box_i_agree: str = '[data-wi=user-agreement] #input-177'
        self.__check_box_false: str = '[data-wi=user-agreement] [aria-checked=false]'
        self.__username_entry_field: str = '[data-wi=user-name] #input-125'
        self.__email_entry_field: str = '[data-wi=identificator] [type=email]'
        self.__password_entry_field: str = '[data-wi=password] [name=new-password]'
        self.__link_referal_correctness: str = '[data-wi=referral] [data-wi=message] span.k-text'
        self.__link_referal_entry_field: str = '[data-wi=referral] #input-165'

    # ================= test_check_all_empty_fields ====================================================================
    def get_nav_link(self) -> WebElement:
        return self.find_element(self.__nav, "Зарегистрироваться")

    @property
    def username_form_checking_correctness(self) -> str | None:
        return (self.shadow_root(self.__shadow_host, self.__username_checking_correctness,
                                 "Поле - Имя пользователя - проверка правильности вводимых данных").
                get_attribute('textContent'))

    @property
    def email_form_checking_correctness(self) -> str | None:
        return (self.shadow_root(self.__shadow_host, self.__email_checking_correctness,
                                 "Поле - Электронная почта - проверка правильности вводимых данных").
                get_attribute('textContent'))

    @property
    def password_form_checking_correctness(self) -> str | None:
        return (self.shadow_root(self.__shadow_host, self.__password_checking_correctness,
                                 "Поле - Пароль - проверка правильности вводимых данных").
                get_attribute('textContent'))

    def user_agreement_check_box(self) -> WebElement:
        return (self.shadow_root(self.__shadow_host, self.__check_box_i_agree,
                                 'Чек-бокс пользовательское соглашение'))

    def user_agreement_check_box_is_not(self) -> WebElement:
        return (self.shadow_root(self.__shadow_host, self.__check_box_false,
                                 'Чек-бокс пользовательское соглашение'))

    @property
    def user_agreement_check_box_is_enabled(self):
        return self.user_agreement_check_box_is_not().is_enabled()

    def submit_button(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__submit_button,
                                "Кнопка - Далее")

    def click_submit_button(self) -> None:
        with allure.step("Нажать кнопку 'Далее'"):
            return self.submit_button().click()

    def click_submit_button_check_box(self):
        self.click_submit_button()
        self.click_check_box()

    def checking_check_box_activity(self) -> bool:
        return self.user_agreement_check_box().is_selected()

    def click_check_box(self) -> None:
        return self.user_agreement_check_box().click()

    def password_save_screenshot(self, name_folder):
        os.makedirs(os.path.join(os.path.dirname(name_folder)), exist_ok=True)
        self.driver.save_screenshot(os.path.join(name_folder))

    # ================= test_field_username ====================================================================
    def username_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__username_entry_field,
                                "Поле - Имя пользователя - ввод данных")

    def username_entry_field_list(self, username_parameter_entry_list) -> None:
        with allure.step("Поле username - вставляем параметры"):
            return self.username_input_entry_field().send_keys(username_parameter_entry_list)

    def username_text_from_field(self):
        with allure.step("Поле username - получаем введенные данные"):
            return self.username_input_entry_field().get_attribute('value')

    # def password_entry_field(self, password_valid_value: str) -> None:
    #     return self.password_input_entry_field().send_keys(password_valid_value)

    # ================== test_field_email ==============================================================================

    # def username_entry_field(self, username_entry_field: str) -> None:
    #     return self.username_input_entry_field().send_keys(username_entry_field)

    def email_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__email_entry_field,
                                "Поле - Электронная почта - ввод данных")

    def email_entry_field_list(self, email_parameter_entry_list) -> None:
        with allure.step("Поле email - вставляем параметры"):
            return self.email_input_entry_field().send_keys(email_parameter_entry_list)

    def email_text_from_field(self):
        with allure.step("Поле email - получаем введенные данные"):
            return self.email_input_entry_field().get_attribute("value")

    def email_entry_field(self, email_valid_value: str) -> None:
        return self.shadow_root(self.__shadow_host, self.__email_entry_field,
                                "Поле - Электронная почта - ввод данных").send_keys(email_valid_value)

    # =============== test_field_password ==============================================================================

    def password_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__password_entry_field,
                                "Поле - Пароль - ввод данных")

    def password_entry_field_list(self, password_parameter_entry_list: str) -> None:
        with allure.step("Поле password - вставляем параметры"):
            return self.password_input_entry_field().send_keys(password_parameter_entry_list)

    def password_text_from_field(self) -> str:
        with allure.step("Поле password - получаем введенные данные"):
            return self.password_input_entry_field().get_attribute("value")

    @property
    def password_entry_field_ru(self) -> str | None:
        return (self.shadow_root(self.__shadow_host, self.__password_checking_correctness_ru, "Поле - RU").
                get_attribute("textContent"))

    def password_visibility_icon(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__password_visibility_icon,
                                "Поле - Пароль - Иконка видимости пароля")

    def password_visibility_icon_click(self) -> None:
        return self.password_visibility_icon().click()

    # def password_visibility_icon_activ(self) -> WebElement:
    #     return self.shadow_root(self.__shadow_host, self.__password_visibility_icon_click, "gjkesdf")

    # =============== test_referal_link ================================================================================

    @property
    def referal_form_checking_correctness(self):
        return (self.shadow_root(self.__shadow_host, self.__link_referal_correctness,
                                 "Поле - Реферальный код - проверка правильности вводимых данных").
                get_attribute('textContent'))

    def referal_input_entry_field(self):
        return self.shadow_root(self.__shadow_host, self.__link_referal_entry_field,
                                "Поле - Реферальный код - ввод данных")

    def referal_entry_field(self, link_referal: str) -> None:
        with allure.step("Поле referal - вставляем параметры"):
            return self.referal_input_entry_field().send_keys(link_referal)

    def referal_text_from_field(self) -> str:
        with allure.step("Поле password - получаем введенные данные"):
            return self.referal_input_entry_field().get_attribute("value")
