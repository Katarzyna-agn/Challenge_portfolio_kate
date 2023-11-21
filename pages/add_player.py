import time

from pages.base_page import BasePage

class AddPlayer(BasePage):
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name ='name']"
    surname_field_xpath = "//*[@name ='surname']"
    phone_field_xpath = "//*[@name ='phone']"
    weight_field_xpath = "//*[@name ='weight']"
    height_field_xpath = "//*[@name ='height']"
    age_field_xpath = "//*[@name ='age']"
    expected_title = 'Add player'
    addplayer_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    def title_of_page(self):
        time.sleep(7)
        assert self.get_page_title(self.addplayer_url) ==self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, email):
        self.field_send_keys(self.name_field_xpath, email)

    def type_in_surname(self, email):
        self.field_send_keys(self.surname_field_xpath, email)

    def type_in_phone(self, email):
        self.field_send_keys(self.phone_field_xpath, email)

    def type_in_weight(self, email):
        self.field_send_keys(self.weight_field_xpath, email)

    def type_in_height(self, email):
        self.field_send_keys(self.height_field_xpath, email)

    def type_in_age(self, email):
        self.field_send_keys(self.age_field_xpath, email)

