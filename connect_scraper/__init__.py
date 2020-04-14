from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
from .classes import Classes

CHROME_DRIVER_PATH = None
HOMEPAGE_LINK = "https://connect.det.wa.edu.au/group/students/ui/overview"
PROFILE_LINK = (
    "https://connect.det.wa.edu.au/group/students/ui/my-settings/profile"
)
ASSESSMENT_OUTLINES_LINK = "https://connect.det.wa.edu.au/group/students/ui/my-settings/assessment-outlines"  # noqa


class ConnectScraper:
    def __init__(self, username: str, password: str, *, headless=True):
        self.__username = username
        self.__password = password

        global CHROME_DRIVER_PATH

        if CHROME_DRIVER_PATH is None:
            import chromedriver_autoinstaller

            CHROME_DRIVER_PATH = chromedriver_autoinstaller.install()

        options = Options()
        options.add_experimental_option(
            "prefs",
            {
                "download.default_directory": os.path.abspath("downloads"),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )
        if headless:
            options.add_argument("--disable-gpu")
            options.add_argument("--headless")
            options.add_argument("--hide-scrollbars")
            options.add_argument("--log-level=3")  # fatal
            self.browser = webdriver.Chrome(
                executable_path=CHROME_DRIVER_PATH, options=options
            )
        else:
            self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

        self.__classes = Classes(self)

    def __del__(self):
        self.browser.quit()

    @property
    def classes(self):
        return self.__classes

    @property
    def homePage(self):
        from .homepage import HomePage

        return HomePage(self)

    def login(self):
        self.browser.get(HOMEPAGE_LINK)
        usernameBox = self.browser.find_element(By.ID, "ssousername")
        usernameBox.send_keys(self.__username)
        passwordBox = self.browser.find_element(By.ID, "password")
        passwordBox.send_keys(self.__password)
        checkBox = self.browser.find_element(By.NAME, "acceptterms")
        checkBox.click()
        loginButton = self.browser.find_element(By.ID, "login")
        loginButton.click()
        # The homepage has loaded enough that we know
        # we've succesfully logged in.
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("connect.det.wa.edu.au")
        )

    def isLoggedIn(self, url: str) -> bool:
        self.browser.get(url)
        try:
            WebDriverWait(self.browser, 5).until(
                EC.url_contains("connect.det.wa.edu.au")
            )
        except TimeoutError:
            return False
        finally:
            return True

    def get(self, url: str, login=True):
        if not self.isLoggedIn(url):
            self.login()
            self.browser.get(url)

    def getFirstName(self):
        self.get(PROFILE_LINK)
        firstNameXPATH = '//*[@id="v-profileportlet_WAR_connectrvportlet_INSTANCE_rGfEXr1VmpqE_LAYOUT_228"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div/div'  # noqa
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, firstNameXPATH))
        )
        return self.browser.find_element(By.XPATH, firstNameXPATH,).text

    def getLastName(self):
        self.get(PROFILE_LINK)
        lastNameXPATH = '//*[@id="v-profileportlet_WAR_connectrvportlet_INSTANCE_rGfEXr1VmpqE_LAYOUT_228"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div'  # noqa
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, lastNameXPATH))
        )
        return self.browser.find_element(By.XPATH, lastNameXPATH,).text

    def getEmail(self):
        self.get(PROFILE_LINK)
        emailXPATH = '//*[@id="v-profileportlet_WAR_connectrvportlet_INSTANCE_rGfEXr1VmpqE_LAYOUT_228"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div'  # noqa
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((By.XPATH, emailXPATH))
        )
        return self.browser.find_element(By.XPATH, emailXPATH,).text

    from .assessmentOutlines import getAssessmentOutlines
