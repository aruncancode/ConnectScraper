from . import CLASSES_LINK, BASE_CLASS_LINK
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Class:
    def __init__(
        self, parent, *, name: str, room: str, locked: bool, link: str,
    ):
        self.__parent = parent
        self.__name = name
        self.__room = room
        self.__locked = locked
        self.__link = link
        self.__id = int(
            self.__link.replace(
                BASE_CLASS_LINK + "summary?coisp=DomainSchoolClass:", ""
            )
        )

    @property
    def name(self):
        return self.__name

    @property
    def room(self):
        return self.__room

    @property
    def locked(self):
        return self.__locked

    @property
    def link(self):
        return self.__link

    @property
    def ID(self):
        return self.__id

    # TODO: make some methods


class Classes:
    def __init__(self, classes: [Class]):
        self.__list = classes
        self.__lastUpdate = datetime.now()

    @property
    def list(self):
        return self.__list

    @property
    def lastUpdate(self):
        return self.__lastUpdate

    def getClassByName(self, name: str) -> Class:
        for clss in self.__list:
            if clss.name == name:
                return clss
        return None

    def getClassByID(self, id: int) -> Class:
        for clss in self.__list:
            if clss.id == id:
                return clss
        return None


def getClassses(self, update=False) -> [Class]:
    if update:

        classGroupXPATH = '//*[@id="v-schoolclassmetricssummaryportlet_WAR_connectrvportlet_INSTANCE_mqpJ9Wlttawi_LAYOUT_216"]/div/div[2]/div[2]/div[1]/div'  # noqa

        def loadClasses():
            self.get(CLASSES_LINK)
            WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, classGroupXPATH + "[1]",)
                )
            )

        loadClasses()
        noOfClasses = len(
            self.browser.find_elements(By.XPATH, classGroupXPATH,)
        )
        classes = []
        i = 1
        while i <= noOfClasses:
            clss = self.browser.find_element(
                By.XPATH, f"{classGroupXPATH}[{i}]/div[1]",
            )
            raw = clss.text.split("\n")
            room = None if len(raw) == 2 else raw[1]
            locked = (
                False
                if "unlocked" in raw[1 if room is None else 2].lower()
                else True
            )
            clss.find_element(By.XPATH, "./div[2]/div[1]").click()
            WebDriverWait(self.browser, 30).until(
                EC.url_contains(BASE_CLASS_LINK)
            )
            link = (
                BASE_CLASS_LINK
                + "summary?coisp=DomainSchoolClass:"
                + self.browser.current_url.split("#")[0]
                .replace(BASE_CLASS_LINK, "")
                .split(":")[1]
            )
            classes.append(
                Class(self, name=raw[0], room=room, locked=locked, link=link,)
            )
            loadClasses()
            i += 1
        self.__classes = classes

    return self.__classes
