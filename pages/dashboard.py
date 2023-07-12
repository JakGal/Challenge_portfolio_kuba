import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//div[@class='MuiToolbar-root MuiToolbar-regular MuiToolbar-gutters']"
    players_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div"
    matches_count_xpath = "//*[text()='Matches count']"
    players_button_xpath = "//div[@class='MuiListItemText - root jss29 jss31']"
    last_created_player_xpath = "//*[text()='Last created player']"
    logo_scouts_panel_xpath = "//div[@title='Logo Scouts Panel']"
    reports_count_xpath = "//div[text()='Reports count']"
    add_player_button_xpath = "//a[@href='/en/players/add']"
    activity_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
    last_updated_player_field_xpath = "//div//h6[text()='Last updated player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    add_player_from_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    add_a_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_a_player_xpath)

