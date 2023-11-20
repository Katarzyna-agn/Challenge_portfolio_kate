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
    main_page_sidebar_xpath = "//*[text()='Main page' or text()='Strona główna']"
    players_sidebar_xpath = "//*[text()='Players' or text()='Gracze']"
    testers_00_snizhana_sidebar_xpath = "//ul[2]/div[1]/div[2]/span"
    matches_sidebar_xpath = "//ul[2]/div[2]/div[2]/span"
    reports_sidebar_xpath = "//ul[2]/div[3]/div[2]/span"
    change_language_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"


pass
