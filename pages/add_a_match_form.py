from pages.base_page import BasePage


class AddAmatchForm(BasePage):
    my_team_xpath = "//*[@name='myTeam']"
    enemy_team_xpath = "//*[@name='enemyTeam']"
    my_team_score_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_xpath = "//*[@name='enemyTeamScore']"
    date_xpath = "//*[@name='date']"
    match_at_home_xpath = "//*[@name='matchAtHome' and @ value = 'true']"
    match_out_home_xpath = "//*[@name='matchAtHome' and @ value = 'false']"
    tshirt_color_xpath = "//*[@name='tshirt']"
    league_xpath = "//*[@name='league']"
    time_played_xpath = "//*[@name='timePlayed']"
    number_xpath = "//*[@name= 'number']"
    web_match_xpath = "//*[@name= 'webMatch']"
    general_xpath = "//*[@name='general']"
    rating_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[@type= 'submit']"
    clear_button_xpath = "//*[text()='Clear']"


pass
