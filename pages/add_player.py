import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AddPlayer(BasePage):
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name ='name']"
    surname_field_xpath = "//*[@name ='surname']"
    phone_field_xpath = "//*[@name ='phone']"
    weight_field_xpath = "//*[@name ='weight']"
    height_field_xpath = "//*[@name ='height']"
    age_field_xpath = "//*[@name ='age']"
    leg_ddown_xpath = "//*[@id='mui-component-select-leg']"
    un_list_of_legs_xpath = "//div[3]/ul"
    right_leg_xpath = "//div[3]/ul/li[1]"
    left_leg_xpath = "//div[3]/ul/li[2]"
    club_xpath = "//div[9]/div/div/input"
    level_xpath = "//div[10]/div/div/input"
    main_position_xpath = "//div[11]/div/div/input"
    second_position_xpath = "//div[12]/div/div/input"
    district_ddown_xpath = "//*[@id='mui-component-select-district']"
    un_list_of_districts_xpath = "//div[3]/ul"
    Masovia_district_xpath = "//ul/li[7]"
    achievements_xpath = "//div[14]/div/div/input"
    submit_button_xpath = "//*[@type ='submit']"
    expected_title = 'Add player'
    addplayer_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page(self):
        assert self.get_page_title(self.addplayer_url) ==self.expected_title
        time.sleep(5)

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)


    def select_leg(self, leg):
        self.click_on_the_element(self.leg_ddown_xpath)
        self.wait_for_visibility_of_element_located(self.un_list_of_legs_xpath)
        if leg == "Right leg":
            self.click_on_the_element(self.right_leg_xpath)


        else:
            self.click_on_the_element(self.left_leg_xpath)


    def type_in_club(self, club):
        self.field_send_keys(self.club_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_xpath, level)

    def type_in_main_position(self, position):
        self.field_send_keys(self.main_position_xpath, position)

    def type_in_second_position(self, position):
        self.field_send_keys(self.second_position_xpath, position)

    def click_on_the_district_dd(self):
        self.click_on_the_element(self.district_ddown_xpath)
        self.wait_for_visibility_of_element_located(self.un_list_of_districts_xpath)

    def click_on_the_Masovia(self):
        self.click_on_the_element(self.Masovia_district_xpath )


    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_xpath, achievements)


    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
        time.sleep(10)#poprawić



