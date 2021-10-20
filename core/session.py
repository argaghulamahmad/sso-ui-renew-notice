import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Session:
    SSO_LOGIN_URL = "https://sso.ui.ac.id/cas/login"
    CHANGE_PASSWORD = "https://beranda.ui.ac.id/personal/profile/changepassword"

    def __init__(self, ):
        load_dotenv()

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-dev-shm-usage")
        options.headless = True

        # Getting the chromedriver from cache or download it from internet
        print("Getting ChromeDriver ...")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.browser.set_window_size(1250, 750)

    def login_sso(self, ):
        try:
            self.browser.get(self.SSO_LOGIN_URL)

            username_input_field = self.browser.find_element(By.ID, "username")
            username_input_field.clear()
            sso_username = os.getenv("SSO_USERNAME")
            username_input_field.send_keys(sso_username)

            password_input_field = self.browser.find_element(By.ID, "password")
            password_input_field.clear()
            sso_password = os.getenv("SSO_PASSWORD")
            password_input_field.send_keys(sso_password)

            xpath_submit_button = "(.//*[normalize-space(text()) and normalize-space(.)='Enter your username and " \
                                  "password'])[ " \
                                  "1]/following::button[1]"
            self.browser.find_element(By.XPATH,
                                      xpath_submit_button).click()
        except NoSuchElementException:
            self.browser.quit()

    def dashboard_ui(self, ):
        try:
            self.browser.get(self.CHANGE_PASSWORD)
            xpath_expired_days_left = "/html/body/div[2]/div[2]/div[1]/div/ul/li[2]/h5/span"
            xpath_login_as = "/html/body/div[2]/div[2]/div[1]/div/ul/li[1]"
            expired_days_left_element = self.browser.find_element(By.XPATH, xpath_expired_days_left)
            login_as_element = self.browser.find_element(By.XPATH, xpath_login_as)
            print(expired_days_left_element.text)
            print(login_as_element.text)
        except NoSuchElementException:
            self.browser.quit()

    def process(self, ):
        self.login_sso()
        self.dashboard_ui()
        self.browser.quit()
