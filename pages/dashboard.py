from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Main page' or text()='Strona główna']"
    players_xpath = "//*[text()='Players' or text()='Gracze']"
    change_language_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"
    players_count_xpath = "//*[text()='Players count' or text()='Ilość graczy']"
    matches_count_xpath = "//*[text()='Matches count' or text()='Ilość meczy']"
    reports_count_xpath = "//*[text()='Reports count' or text()='Ilość raportów']"
    events_count_xpath = "//*[text()='Events count' or text()='Ilość akcji']"
    dev_team_contact_xpath = "//*[text()= 'Dev team contact']"
    add_player_xpath = "//*[text()='Add player' or text()='Dodaj gracza']"
    activity_xpath = "//*[text()='Activity' or text()='Aktywnosć']"
    last_created_player_xpath = "//*[text()='Last created player' or text()='Ostatnio stworzony gracz']"
    last_updated_player_xpath = "//*[text()='Last updated player' or text()='Ostatnio zaaktualizowany gracz']"
    last_created_match_xpath = "//*[text()='Last created match' or text()='Ostatnio stworzony mecz']"
    last_updated_match_xpath = "//*[text()='Last updated match' or text()='Ostatnio zaaktualizowany mecz']"
    last_updated_report_xpath = "//*[text()='Last updated report' or text()='Ostatnio zaaktualizowany raport']"


pass
