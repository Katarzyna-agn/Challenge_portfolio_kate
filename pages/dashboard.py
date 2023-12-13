import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//ul[1]/div[1]/div[2]/span"
    players_xpath = "//ul[1]/div[2]/div[2]/span"
    change_language_xpath = "//ul[2]/div[1]/div[2]/span"
    sign_out_xpath = "//ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//*[text()='Players count' or text()='Ilość graczy']"
    matches_count_xpath = "//*[text()='Matches count' or text()='Ilość meczy']"
    reports_count_xpath = "//*[text()='Reports count' or text()='Ilość raportów']"
    events_count_xpath = "//*[text()='Events count' or text()='Ilość akcji']"
    dev_team_contact_xpath = "//*[text()= 'Dev team contact']"
    add_player_xpath = "//div[2]/div/div/a/button/span[1]"
    activity_xpath = "//div[3]/div/div/h2"
    last_created_player_xpath = "//div/div/h6[1]"
    last_updated_player_xpath = "//div/div/h6[2]"
    last_created_match_xpath = "//div/div/h6[3]"
    last_updated_match_xpath = "//div/div/h6[4]"
    last_updated_report_xpath = "//div/div/h6[5]"
    last_added_player_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    futbol_kolektyw_logo_xpath = "//*[@title = 'Logo Scouts Panel']"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://dareit.futbolkolektyw.pl/en'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title() == self.expected_title


    def click_on_the_add_player(self):
        self.click_on_the_element(self.add_player_xpath)


pass
