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

        temp_db["Title"].append(event_title.text)
        temp_db["Body"].append(" ".join(event_body.text.split()))
        temp_db["Date"].append("6/4/2020")
        temp_db["Class"].append()

        return temp_db

    def submissions(self):
        sub_db = {
            "Name": [],
            "Date": [],
            "Due Date": [],
            "Class": [],
            "Status": [],
        }

        submission_name = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-nextsubmissionportlet_WAR_connectrvportlet_INSTANCE_hxAR8l8SbS5Q_LAYOUT_215"]/div/div[2]/div/div[2]/div/div/div/div[1]',
        ).get_attribute("innerHTML")

        submission_class = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-nextsubmissionportlet_WAR_connectrvportlet_INSTANCE_hxAR8l8SbS5Q_LAYOUT_215"]/div/div[2]/div/div[2]/div/div/div/div[2]',
        ).get_attribute("innerHTML")

        submission_due_date = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-nextsubmissionportlet_WAR_connectrvportlet_INSTANCE_hxAR8l8SbS5Q_LAYOUT_215-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div',
        ).get_attribute("innerHTML")

        submission_status = self.browser.find_element(
            By.XPATH,
            '//*[@id="v-nextsubmissionportlet_WAR_connectrvportlet_INSTANCE_hxAR8l8SbS5Q_LAYOUT_215"]/div/div[2]/div/div[2]/div/div/div/div[4]/div[2]',
        ).get_attribute("innerHTML")

        submission_name = soup(submission_name, "html.parser")
        submission_due_date = soup(submission_due_date, "html.parser")

        sub_db["Name"] = submission_name.text
        sub_db["Due Date"] = submission_due_date.text
        sub_db["Date"] = "6/4/2020"
        sub_db["Status"] = submission_status.text
        sub_db["Class"] = submission_class.text

        return sub_db

    def test(self):
        # submission_name = self.browser.find_element(
        #     By.XPATH,
        #     '//*[@id="v-schoolclassmetricssummaryportlet_WAR_connectrvportlet_INSTANCE_mqpJ9Wlttawi_LAYOUT_216"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]',
        # ).get_attribute("value")

        self.browser.get(
            "https://connect.det.wa.edu.au/group/students/ui/my-settings/profile"
        )
        time.sleep(5)

        submission_name_class = self.browser.find_element_by_class_name(
            '//*[@id="v-myclassesminiportlet_WAR_connectrvportlet_INSTANCE_hkO0RfHO0arq_LAYOUT_228"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div'
        )
        return submission_name_class.text
