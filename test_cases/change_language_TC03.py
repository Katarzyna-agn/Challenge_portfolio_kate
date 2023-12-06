import os
import time
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage03(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_change_language_TC03(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.change_language("english")
        user_login.change_language("polski")
        user_login.check_page_text_pl()


    @classmethod
    def tearDown(self):
        self.driver.quit()
