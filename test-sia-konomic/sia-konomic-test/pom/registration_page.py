from selenium.webdriver.remote.webelement import WebElement

from base.base import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__nav: str = '//span[contains(text(),"Зарегистрироваться")]'
        self.__shadow_host: str = 'div.remoteComponent'
        self.__username_checking_correctness: str = '[data-wi=user-name] span.k-text'
        self.__email_checking_correctness: str = '[data-wi=identificator] span.k-text'
        self.__password_checking_correctness: str = '[data-wi=password] span.k-text'
        self.__submit_button: str = '[data-wi=submit-button] span.v-btn__content'
        self.__check_box_i_agree: str = '[data-wi=user-agreement] #input-179'
        self.__username_entry_field: str = '[data-wi=user-name] #input-127'
        self.__email_entry_field: str = '[data-wi=identificator] [type=email]'
        self.__password_entry_field: str = '[data-wi=password] [name=new-password]'
        self.__link_referal_correctness: str = '[data-wi=referral] span.k-text'
        self.__linnk_referal_entry_field: str = '[data-wi=referral] #input-167'

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

    @property
    def user_agreement_check_box(self) -> WebElement:
        return (self.shadow_root(self.__shadow_host, self.__check_box_i_agree,
                                 'Чек-бокс пользовательское соглашение'))

    def submit_button(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__submit_button,
                                "Кнопка - Далее")

    def click_submit_button(self) -> None:
        return self.submit_button().click()

    def click_submit_button_check_box(self) -> None:
        self.submit_button().click()
        self.user_agreement_check_box.click()

    def click_check_box(self) -> None:
        return self.user_agreement_check_box.click()

    @property
    def checking_check_box_activity(self) -> bool:
        return self.user_agreement_check_box.is_selected()

    # ================= test_field_username ====================================================================
    def username_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__username_entry_field,
                                "Поле - Имя пользователя - ввод данных")

    def username_entry_field_list(self, username_parameter_entry_list: list) -> None:
        return self.username_input_entry_field().send_keys(username_parameter_entry_list)

    def email_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__email_entry_field,
                                "Поле - Электронная почта - ввод данных")

    def email_entry_field(self, email_valid_value: str) -> None:
        return self.shadow_root(self.__shadow_host, self.__email_entry_field,
                                "Поле - Электронная почта - ввод данных").send_keys(email_valid_value)

    def password_input_entry_field(self) -> WebElement:
        return self.shadow_root(self.__shadow_host, self.__password_entry_field,
                                "Поле - Пароль - ввод данных")

    def password_entry_field(self, password_valid_value: str) -> None:
        return self.password_input_entry_field().send_keys(password_valid_value)

    # ================== test_field_email ==============================================================================

    def username_entry_field(self, username_entry_field: str) -> None:
        return self.username_input_entry_field().send_keys(username_entry_field)

    def email_entry_field_list(self, email_parameter_entry_list: list) -> None:
        return self.email_input_entry_field().send_keys(email_parameter_entry_list)

    # =============== test_field_password ==============================================================================

    def pasword_entry_field_list(self, password_parameter_entry_list: list) -> None:
        return self.password_input_entry_field().send_keys(password_parameter_entry_list)

    # =============== test_referal_link ================================================================================

    @property
    def referal_form_checking_correctness(self):
        return (self.shadow_root(self.__shadow_host, self.__link_referal_correctness,
                                 "Поле - Реферальный код - проверка правильности вводимых данных").
                get_attribute('textContent'))

    def referal_input_entry_field(self):
        return self.shadow_root(self.__shadow_host, self.__linnk_referal_entry_field,
                                "Поле - Реферальный код - ввод данных")

    def referal_entry_field(self, link_referal: str) -> None:
        return self.referal_input_entry_field().send_keys(link_referal)
