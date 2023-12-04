import time

from pages.base_page import BasePage


class EditPlayer(BasePage):
    expected_title = 'Edit player John Bianco'
    expected_text_of_box = 'John Bianco'
    title_of_box_xpath = "//ul[2]/div[1]/div[2]/span"
    editplayer_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        self.wait_for_visibility_of_element_located(self.title_of_box_xpath)
        assert self.get_page_title() == self.expected_title

    def check_page_text(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_text_of_box)
