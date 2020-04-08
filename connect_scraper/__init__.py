from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import time
from datetime import date

CHROME_DRIVER_PATH = None


class ConnectScraper:
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
        ).click()
        self.browser.implicitly_wait(2)
        view_notice = self.browser.find_element(
            By.CSS_SELECTOR,
            "#v-latestinformationportlet_WAR_connectrvportlet_INSTANCE_WqBA68MkuxAs_LAYOUT_215-overlays > div.v-window.v-widget.cvr-c-fixed-popup.v-window-cvr-c-fixed-popup.cvr-c-fixed-popup--large.v-window-cvr-c-fixed-popup--large.eds-u-theme-multiplier.v-window-eds-u-theme-multiplier.eds-t-purple.v-window-eds-t-purple.cvr-c-popup.v-window-cvr-c-popup > div > div > div.v-window-contents > div > div > div.eds-c-button-set.v-layout.v-widget.eds-c-button-set--fill.eds-c-button-set-eds-c-button-set--fill.eds-c-button-set--collapse.eds-c-button-set-eds-c-button-set--collapse.eds-c-button-set--inline.eds-c-button-set-eds-c-button-set--inline.cvr-c-popup-button-set.eds-c-button-set-cvr-c-popup-button-set.eds-s-is-last.eds-c-button-set-eds-s-is-last.cvr-c-popup-button-set--xwide > div.v-button.v-widget.eds-o-button.v-button-eds-o-button.cvr-c-popup-action-button.v-button-cvr-c-popup-action-button.eds-o-button--featured.v-button-eds-o-button--featured",
        ).click()
        self.browser.implicitly_wait(1)

        notice_title = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]",
        ).get_attribute("innerHTML")

        notice_body = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div[2]/div[1]",
        ).get_attribute("innerHTML")

        notice_class = self.browser.find_element(
            By.XPATH,
            "/html/body/div[1]/section/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div",
        ).get_attribute("innerHTML")

        notice_body = soup(notice_body, "html.parser")
        notice_title = soup(notice_title, "html.parser")

        temp_db["Title"] = notice_title.text
        temp_db["Body"] = " ".join(notice_body.text.split())
        temp_db["Subject"] = notice_class
        temp_db["Date"] = self.current_date
        temp_db["Person"] = self.__username

        return temp_db

    def get_submissions(self):
        sub_db = {}

        self.browser.get("https://connect.det.wa.edu.au/")
        self.browser.implicitly_wait(2)

        open_submission_button = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/section/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]",
        ).click()

        self.browser.implicitly_wait(2)
        view_submission = self.browser.find_element(
            By.CSS_SELECTOR,
            "#v-nextsubmissionportlet_WAR_connectrvportlet_INSTANCE_hxAR8l8SbS5Q_LAYOUT_215-overlays > div.v-window.v-widget.cvr-c-fixed-popup.v-window-cvr-c-fixed-popup.cvr-c-fixed-width-popup.v-window-cvr-c-fixed-width-popup.cvr-c-fixed-width-popup--medium.v-window-cvr-c-fixed-width-popup--medium.cvr-c-popup.v-window-cvr-c-popup > div > div > div.v-window-contents > div > div > div.eds-c-button-set.v-layout.v-widget.eds-c-button-set--fill.eds-c-button-set-eds-c-button-set--fill.eds-c-button-set--collapse.eds-c-button-set-eds-c-button-set--collapse.eds-c-button-set--inline.eds-c-button-set-eds-c-button-set--inline.cvr-c-popup-button-set.eds-c-button-set-cvr-c-popup-button-set.eds-s-is-last.eds-c-button-set-eds-s-is-last > div.v-button.v-widget.eds-o-button.v-button-eds-o-button.cvr-c-popup-action-button.v-button-cvr-c-popup-action-button.eds-o-button--featured.v-button-eds-o-button--featured",
        ).click()
        self.browser.implicitly_wait(1)

        submission_name = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[1]",
        ).get_attribute("innerHTML")

        submission_class = self.browser.find_element(
            By.XPATH,
            "/html/body/div[1]/section/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div",
        ).get_attribute("innerHTML")

        submission_due_date = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]",
        ).get_attribute("innerHTML")

        submission_status = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[5]/div[2]",
        ).get_attribute("innerHTML")

        submission_status = soup(submission_status, "html.parser")

        submission_body = self.browser.find_element(
            By.XPATH,
            "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div[6]",
        ).get_attribute("innerHTML")

        submission_body = soup(submission_body, "html.parser")

        sub_db["Title"] = submission_name
        sub_db["Due Date"] = submission_due_date
        sub_db["Date"] = self.current_date
        sub_db["Status"] = submission_status.text
        sub_db["Class"] = submission_class
        sub_db["Body"] = submission_body.text[:-2]
        sub_db["Person"] = self.__username

        return sub_db

    def get_marks(self):
        marks_db = {}

        self.browser.get(
            "https://connect.det.wa.edu.au/group/students/ui/my-settings/assessment-outlines"
        )

        time.sleep(5)

        for e in range(1, 5):  # subjects
            button_link = (
                "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[%s]/div/div[2]/div/div[4]/div/div/div[1]"
                % str(e)
            )
            data_link = (
                "/html/body/main/div/div[2]/div/div/div/div/section/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[%s]/div/div[2]/div/div[4]/div/div[2]"
                % str(e)
            )
            self.browser.find_element(By.XPATH, button_link).click()
            time.sleep(5)
            print("opened data")
            test = self.browser.find_element(By.XPATH, data_link).get_attribute(
                "innerHTML"
            )
            print("scraped data")
            time.sleep(1)

            test = soup(test, "html.parser")
            test = test.text.replace("Created with Highstock 4.2.6", " ")
            marks_db[str(e)] = test

        return marks_db


#
# extremely messy, needs to be fixed up.
