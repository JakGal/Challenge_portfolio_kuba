import os
import unittest
import time

from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.Add_A_Player import AddAPlayer


class TestAddAPlayerPage(unittest.TestCase):
    add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    add_player_form_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"


    @classmethod
    def setUp(cls):
        os.chmod(DRIVER_PATH, 755)
        cls.driver_service = Service(executable_path=DRIVER_PATH)
        cls.driver = webdriver.Chrome(service=cls.driver_service)
        cls.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        cls.driver.fullscreen_window()
        cls.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        time.sleep(5)
    @classmethod
    def tearDown(self):
        self.driver.quit()

