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
        options.add_experimental_option('w3c', False)

        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")

        options.add_argument("--lang=en-GB")

        options.headless = False

        # Getting the chromedriver from cache or download it from internet
        print("Getting ChromeDriver ...")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.browser.set_window_size(1250, 750)

        # clear the console based on the operating system you're using
        os.system('cls' if os.name == 'nt' else 'clear')

    def login_sso(self, ):
        try:
            self.browser.get(self.SSO_LOGIN_URL)

            username_input_field = self.browser.find_element(By.ID, "username")
            sso_username = os.getenv("SSO_USERNAME")
            username_input_field.send_keys(sso_username)
            password_input_field = self.browser.find_element(By.ID, "password")
            password_input_field.clear()
            sso_password = os.getenv("SSO_PASSWORD")
            password_input_field.send_keys(sso_password)
            self.browser.find_element(By.XPATH,
                                      "(.//*[normalize-space(text()) and normalize-space(.)='Enter your username and "
                                      "password'])[ "
                                      "1]/following::button[1]").click()
        except NoSuchElementException:
            self.browser.quit()

    def dashboard_ui(self, ):
        try:
            self.browser.get(self.CHANGE_PASSWORD)
            list_info = self.browser.find_element(By.ID, "sparks-info")
            for info in list_info:
                print(info.text)
        except NoSuchElementException:
            self.browser.quit()

    def process(self, ):
        self.login_sso()
        self.dashboard_ui()
        self.browser.quit()
