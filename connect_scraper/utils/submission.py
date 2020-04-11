from .. import BASE_SUBMISSIONS_LINK, webdriver, By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


class Submission:
    def __init__(
        self,
        classId: int,
        title: str,
        dueDate: datetime,
        status: str,
        isOpen: bool,
        rawBody: str,
    ):
        self.__classID = classId
        self.__title = title
        self.__dueDate = dueDate
        self.__status = status
        self.__isOpen = isOpen
        self.__rawBody = rawBody
        self.__hashID = hash(str(self.__classID) + str(self.__title))

    @property
    def classID(self):
        return self.__classID

    @property
    def title(self):
        return self.__title

    @property
    def dueDate(self):
        return self.__dueDate

    @property
    def status(self):
        return self.__status

    @property
    def isOpen(self):
        return self.__isOpen

    @property
    def rawBody(self):
        return self.__rawBody

    @property
    def hashID(self):
        return self.__hashID

    @staticmethod
    def scrape(browser: webdriver.Chrome):
        submissionBox = browser.find_element(
            By.XPATH,
            '//*[@id="v-submissionportlet_WAR_connectrvportlet_INSTANCE_IQdBhuiMMrFp_LAYOUT_248"]/div/div[2]/div[3]/div/div[2]',  # noqa
        )
        classId = int(
            browser.current_url.replace(BASE_SUBMISSIONS_LINK, "").split("&")[0]
        )
        dueDateText = submissionBox.find_element(
            By.XPATH, "./div[2]/div[2]",
        ).text
        # Format: Friday, 10 April 2020 @11:30PM
        dueDate = datetime.strptime(dueDateText, "%A, %d %B %Y @%I:%M%p")
        title = submissionBox.find_element(By.XPATH, "./div[1]",).text
        try:
            status = submissionBox.find_element(
                By.XPATH, "./div[5]/div[3]"
            ).text
        except NoSuchElementException:
            status = submissionBox.find_element(
                By.XPATH, "./div[5]/div[2]"
            ).text
        isOpen = (
            True
            if submissionBox.find_element(
                By.XPATH, "./div[5]/div[1]",
            ).text.strip()
            == "Open"
            else False
        )
        rawBody = submissionBox.find_element(
            By.XPATH, "./div[6]",
        ).get_attribute("innerHTML")
        return Submission(classId, title, dueDate, status, isOpen, rawBody)
