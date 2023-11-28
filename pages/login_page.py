from pages.base_page import BasePage
import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remaind_password_xpath = "//div[1]/a"
    select_language_button_xpath = "//div[2]/div/div"
    english_option_xpath = "//div[3]/ul/li[2]"
    polish_option_xpath = "//div[3]/ul/li[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"
    header_of_box_xpath = "//div[1]/h5"
    excepted_header_of_box = "Scouts Panel"
    remaind_password_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'
    expected_title_of_remaind_password = "Remind password"
    wait = WebDriverWait(driver, 10)

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
        time.sleep(3)

    def type_in_password(self,password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_remaind_password(self):
        self.click_on_the_element(self.remaind_password_xpath)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_page_header(self):
        self.assert_element_text(self.driver, self.header_of_box_xpath, self.excepted_header_of_box)

    def title_of_remaind_password(self):
        assert self.get_page_title(self.remaind_password_url) == self.expected_title_of_remaind_password
        time.sleep(3)

    def select_language(self, language):
        self.wait_for_element_to_be_clickable(self.select_language_button_xpath)
        self.click_on_the_element(self.select_language_button_xpath)
        if language =="english":
            self.click_on_the_element(self.english_option_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.polish_option_xpath)
            self.click_on_the_element(self.polish_option_xpath)
            time.sleep(3)




