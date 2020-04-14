from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import List


CLASSES_LINK = "https://connect.det.wa.edu.au/group/students/ui/classes"
BASE_CLASS_LINK = "https://connect.det.wa.edu.au/group/students/ui/class/"


class ClassPage:
    page = None

    def __init__(self, parent):
        self.parent = parent
        self.connect = self.parent.connect
        self.link = self.pageLink() if self.page is not None else None

    def pageLink(self) -> str:
        return (
            BASE_CLASS_LINK
            + self.page
            + "?coisp=DomainSchoolClass:"
            + str(self.parent.id)
        )


class Notices(ClassPage):
    def __init__(self, parent):
        self.page = "announcements"
        super().__init__(parent)


class Submissions(ClassPage):
    def __init__(self, parent):
        self.page = "submissions"
        super().__init__(parent)


class Class:
    def __init__(
        self,
        connect,
        *,
        name: str,
        room: str = None,
        locked: bool = None,
        id: int,
    ):
        self.connect = connect
        self.__name = name
        self.__room = room
        self.__locked = locked
        self.__id = id

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
    def id(self):
        return self.__id

    @property
    def notices(self):
        return Notices(self)

    @property
    def submissions(self):
        return Submissions(self)


class Classes:
    def __init__(self, connect):
        self.connect = connect
        self.__list = []
        self.__lastUpdate = None

    def __getitem__(self, key):
        return self.__list[key]

    def update(self):
        classGroupXPATH = '//*[@id="v-schoolclassmetricssummaryportlet_WAR_connectrvportlet_INSTANCE_mqpJ9Wlttawi_LAYOUT_216"]/div/div[2]/div[2]/div[1]/div'  # noqa

        def loadClasses():
            self.connect.get(CLASSES_LINK)
            WebDriverWait(self.connect.browser, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, classGroupXPATH + "[1]",)
                )
            )

        loadClasses()
        noOfClasses = len(
            self.connect.browser.find_elements(By.XPATH, classGroupXPATH,)
        )
        classes = []
        i = 1
        while i <= noOfClasses:
            clss = self.connect.browser.find_element(
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
            WebDriverWait(self.connect.browser, 30).until(
                EC.url_contains(BASE_CLASS_LINK)
            )
            id = int(
                self.connect.browser.current_url.replace(BASE_CLASS_LINK, "")
                .split("#")[0]
                .split(":")[1]
            )
            classes.append(
                Class(
                    self.connect, name=raw[0], room=room, locked=locked, id=id
                )
            )
            loadClasses()
            i += 1
        self.__list = classes
        self.__lastUpdate = datetime.now()
        return self

    @property
    def list(self) -> List[Class]:
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
