from . import ASSESSMENT_OUTLINES_LINK
import time


class Mark:
    def __init__(
        self, name: str, rawScore: [float, float], weightedMark: [float, float]
    ):
        self.__name = name
        self.__rawScore = rawScore
        self.__weightedMark = weightedMark

    @property
    def name(self):
        return self.__name

    @property
    def rawScore(self):
        return self.__rawScore

    @property
    def weightedMark(self):
        return self.__weightedMark

    @staticmethod
    def ser(pair):
        return f"{str(pair[0])}/{str(pair[1])}"

    @staticmethod
    def deser(str):
        def convrt(n):
            if n == "None":
                return None
            else:
                return float(n)

        return list(map(convrt, str.split("/")))


class MarksGroup:
    def __init__(self, name: str, teacher: str, marks: dict):
        self.__name = name
        self.__teacher = teacher
        self.__marks = marks
        self.__hashID = hash(self.__name + self.__teacher + self.__obj)

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def marks(self):
        return self.__marks

    @property
    def hashID(self):
        return self.__hashID


def getAssessmentOutlines(self):
    self.get(ASSESSMENT_OUTLINES_LINK)
    groupsXPATH = '//*[@id="v-studentassessmentoutlineportlet_WAR_connectrvportlet_INSTANCE_RpxlkUYQqwjo_LAYOUT_233"]/div/div[2]/div[3]/div/div/div[1]/div'  # noqa
    WebDriverWait(self.browser, 30).until(
        EC.presence_of_element_located((By.XPATH, groupsXPATH))
    )
    groups = self.browser.find_elements(By.XPATH, groupsXPATH)
    groupedMarks = []
    for group in groups:
        name = group.find_element(By.XPATH, "./div/div[1]/div")
        teacher = group.find_element(By.XPATH, "./div/div[2]/div/div[1]/div[1]")
        group.find_element(By.XPATH, "./div/div[2]/div/div[4]/div/div").click()
        WebDriverWait(group, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "./div/div[2]/div/div[4]/div/div[2]/div/div/div/div")
            )
        )
        sections = group.find_elements(
            By.XPATH, "./div/div[2]/div/div[4]/div/div[2]/div/div[1]/div/div"
        )
        lastHeader = None
        lastSectHeader = None
        groupDict = {lastHeader: {lastSectHeader: []}}
        for section in sections:
            time.sleep(0.1)
            attr = section.get_attribute("class")
            if "cvr-c-task-group" in attr:  # Header
                lastHeader = section.find_element(By.XPATH, "./div[1]").text
                groupDict[lastHeader] = {None: []}
            elif "v-label-undef-w" in attr:  # Section Header
                lastSectHeader = section.text
                groupDict[lastHeader][lastSectHeader] = []
            elif "cvr-c-task" in attr:  # Mark
                desc = section.find_element(By.XPATH, "./div[1]").text
                markBox = section.find_element(By.XPATH, "./div[3]/div[1]")
                marks = markBox.find_element(
                    By.XPATH, "./div[1]"
                ).text.lower().split("out of") + markBox.find_element(
                    By.XPATH, "./div[2]"
                ).text.lower().split(
                    "out of"
                )
                newMarks = []
                for mark in marks:
                    try:
                        newMarks.append(float(mark))
                    except ValueError:
                        newMarks.append(None)
                groupDict[lastHeader][lastSectHeader].append(
                    Mark(desc, newMarks[0:2], newMarks[2:4])
                )
            else:
                raise Exception("Found something odd in the group.")
        groupedMarks.append(MarksGroup(name, teacher, groupDict))
    return groupedMarks
