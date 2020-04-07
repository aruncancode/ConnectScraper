from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import time
from datetime import date

CHROME_DRIVER_PATH = None


class ConnectApi:
    def __init__(self, username: str, password: str, *, headless=True):
        if not isinstance(username, str):
            raise TypeError("The username parameter must be a string.")
        if not isinstance(password, str):
            raise TypeError("The password parameter must be a string.")

        self.__username = username
        self.__password = password
        self.current_date = str(
            date.today()
        )  # i can't be bothered doing the self.__ thing

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

    def get_notices(self):
        temp_db = {}
        notice_btn = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[1]/div[1]/div/div/div[3]/section/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/span/span",
        )
        notice_btn.click()
        time.sleep(1)

        event_title = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/div[1]',
        ).get_attribute("innerHTML")

        event_body = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/div[2]',
        ).get_attribute("innerHTML")

        event_body = soup(event_body, "html.parser")
        event_title = soup(event_title, "html.parser")

        temp_db["Title"] = event_title.text
        temp_db["Body"] = " ".join(event_body.text.split())
        temp_db["Date"] = self.current_date
        temp_db["Person"] = self.__username
        # have to find a way to identify which class the notice came from

        return temp_db

    def get_submissions(self):
        sub_db = {}

        submission_name = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/section/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]",
        ).get_attribute("innerHTML")

        submission_class = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/section/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[2]",
        ).get_attribute("innerHTML")

        submission_due_date = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/section/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]",
        ).get_attribute("innerHTML")

        submission_status = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/section/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div[3]",
        ).get_attribute("innerHTML")
        submission_status = soup(submission_status, "html.parser")

        submission_body = "na"

        sub_db["Title"] = submission_name
        sub_db["Due Date"] = submission_due_date
        sub_db["Date"] = self.current_date
        sub_db["Status"] = submission_status.text
        sub_db["Class"] = submission_class
        sub_db["Body"] = submission_body
        sub_db["Person"] = self.__username

        return sub_db

    def get_marks(self):
        self.browser.get(
            "https://connect.det.wa.edu.au/group/students/ui/my-settings/assessment-outlines"
        )
        time.sleep(2)

        show_details = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div[2]",
        )
        show_details.click()

        submission_name = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div[2]",
        ).get_attribute("innerHTML")

        parsed_data = soup(submission_name, "html.parser")

        return parsed_data.text


# extremely messy, needs to be fixed up.
