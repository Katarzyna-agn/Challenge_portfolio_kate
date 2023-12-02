import time

from pages.base_page import BasePage


class EditPlayer(BasePage):
    expected_title = 'Edit player John Wan'
    expected_text_of_box = 'John Wan'
    title_of_box_xpath = "//*[ text() = 'John Wan']"
    editplayer_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        time.sleep(3)
        assert self.get_page_title() == self.expected_title

    def check_page_text(self):
        self.wait_for_visibility_of_element_located(self.title_of_box_xpath)
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.expected_text_of_box)
