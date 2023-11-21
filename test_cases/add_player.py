import os
import time
import unittest
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT




class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page=Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player()
        addplayer_page=AddPlayer(self.driver)
        addplayer_page.title_of_page()
        addplayer_page.type_in_email('kate@getnada.com')
        addplayer_page.type_in_name('Kate')
        addplayer_page.type_in_surname('Primavera')
        addplayer_page.type_in_phone('444-256-254')
        addplayer_page.type_in_weight('60')
        addplayer_page.type_in_height('180')
        addplayer_page.type_in_age('12.12.1990')
        time.sleep(10)


    @classmethod
    def tearDown(self):
        self.driver.quit()