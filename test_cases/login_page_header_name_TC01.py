import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage01(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_page_header_name_TC01(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_page_text()

    @classmethod
    def tearDown(self):
        self.driver.quit()
