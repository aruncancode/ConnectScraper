from selenium import webdriver
from selenium.webdriver.common.by import By

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

            CHROME_DRIVER_PATH = chromedriver_autoinstaller.install(cwd=True)
        # The browser will close when it is garbage collected by the
        # interpreter. This shouldn't be a problem since it will stay
        # open as long as you are using it.
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
