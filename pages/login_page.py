from pages.base_page import BasePage
import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_xpath = "//div[1]/a"
    change_language_button_xpath = "//div[2]/div/div"
    un_list_language_xpath = "//div[3]/ul"
    english_option_xpath = "//div[3]/ul/li[2]"
    polish_option_xpath = "//div[3]/ul/li[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//div[1]/h5"
    expected_text_of_box = "Scouts Panel"
    expected_text_of_przyphaslo = "Przypomnij hasło"
    remind_password_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'
    remind_password_text_xpath = "//div[1]/h5"
    expected_title_of_remind_password = "Remind password"
    wait = WebDriverWait(driver, 10)


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_remind_password(self):
        self.click_on_the_element(self.remind_password_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title() == self.expected_title

    def check_page_text(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_text_of_box)

    def check_page_text_pl(self):
        self.assert_element_text(self.driver, self.remind_password_xpath, self.expected_text_of_przyphaslo)

    def title_of_remind_password(self):
        assert self.get_page_title() == self.expected_title_of_remind_password
        self.wait_for_visibility_of_element_located(self.remind_password_text_xpath )


    def change_language(self, language):
        self.click_on_the_element(self.change_language_button_xpath)
        if language == "english":
            self.wait_for_visibility_of_element_located(self.un_list_language_xpath)
            self.click_on_the_element(self.english_option_xpath)


        else:
            self.click_on_the_element(self.polish_option_xpath)
            self.wait_for_visibility_of_element_located(self.change_language_button_xpath)
