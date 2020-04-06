from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import time

CHROME_DRIVER_PATH = None


class ConnectApi:
    def __init__(self, username: str, password: str, *, headless=True):
        if not isinstance(username, str):
            raise TypeError("The username parameter must be a string.")
        if not isinstance(password, str):
            raise TypeError("The password parameter must be a string.")

        self.__username = username
        self.__password = password

        global CHROME_DRIVER_PATH

        if CHROME_DRIVER_PATH is None:
            import chromedriver_autoinstaller

            CHROME_DRIVER_PATH = chromedriver_autoinstaller.install()

        if headless:
            from selenium.webdriver.chrome.options import Options

            options = Options()
            options.add_argument("--disable-gpu")
            options.add_argument("--headless")
            options.add_argument("--hide-scrollbars")
            options.add_argument("--log-level=3")  # fatal
            self.browser = webdriver.Chrome(
                executable_path=CHROME_DRIVER_PATH, options=options
            )
        else:
            self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.browser.get("https://connect.det.wa.edu.au/")
        usernameBox = self.browser.find_element(By.ID, "ssousername")
        usernameBox.send_keys(self.__username)
        passwordBox = self.browser.find_element(By.ID, "password")
        passwordBox.send_keys(self.__password)
        checkBox = self.browser.find_element(By.NAME, "acceptterms")
        checkBox.click()
        loginButton = self.browser.find_element(By.ID, "login")
        loginButton.click()

    def notices(self):
        temp_db = {"Name": [], "Date": [], "Body": []}
        notice_btn = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215"]/div/div[2]/div/div[1]/div[2]/span/span',
        )
        notice_btn.click()
        time.sleep(1)

        event_title = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/b',
        ).get_attribute("innerHTML")

        event_body = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div[1]',
        ).get_attribute("innerHTML")

        event_body = soup(event_body, "html.parser")
        event_title = soup(event_title, "html.parser")

        temp_db["Name"].append(event_title.text)
        temp_db["Body"].append(" ".join(event_body.text.split()))
        temp_db["Date"].append("6/4/2020")

        return temp_db
