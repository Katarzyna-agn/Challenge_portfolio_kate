import time

from pages.base_page import BasePage

class EditPlayer(BasePage):

    expected_title = 'Edit player.......'
    edit_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        time.sleep(7)
        assert self.get_page_title(self.edit_url) ==self.expected_title

