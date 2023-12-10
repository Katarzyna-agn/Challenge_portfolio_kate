import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player import AddPlayer
from pages.edit_player import EditPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer01(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_fill_add_player_form_req_TC05(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_add_player()
        addplayer_page = AddPlayer(self.driver)
        addplayer_page.title_of_page()
        addplayer_page.type_in_name('John')
        addplayer_page.type_in_surname('Bianco')
        addplayer_page.type_in_age('12.12.1992')
        addplayer_page.type_in_main_position('good player')
        addplayer_page.click_on_submit_button()
        editplayer_page = EditPlayer(self.driver)
        editplayer_page.title_of_page()
        editplayer_page.check_page_text()

    @classmethod
    def tearDown(self):
        self.driver.quit()
