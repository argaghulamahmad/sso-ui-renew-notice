import environ
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

env = environ.Env(DEBUG=(bool, False), )
# environ.Env.read_env('.env')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("headless")
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

SSO_LOGIN_URL = "https://sso.ui.ac.id/cas/login"
CHANGE_PASSWORD = "https://beranda.ui.ac.id/personal/profile/changepassword"


def process():
    login_sso()
    dashboard_ui()
    browser.quit()


def login_sso():
    try:
        print("[Info - activity]: Login SSO UI")
        browser.get(SSO_LOGIN_URL)
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys(env("SSO_USERNAME"))
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys(env("SSO_PASSWORD"))
        browser.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Enter your username and password'])["
            "1]/following::button[1]").click()
    except NoSuchElementException:
        browser.quit()


def dashboard_ui():
    try:
        print("[Info - activity]: Change Pass Beranda UI")
        browser.get(CHANGE_PASSWORD)
        print("[Info - activity]: Retrieve Information")
        list_info = browser.find_elements_by_class_name("sparks-info")
        for info in list_info:
            print(info.text)
    except NoSuchElementException:
        browser.quit()


# main method
if __name__ == '__main__':
    process()
