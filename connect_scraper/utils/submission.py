from .. import BASE_SUBMISSIONS_LINK
import hashlib


class Submission:
    def __init__(self, parent, link: str):
        self.__link = link
        self.__classID = int(
            self.link.replace(BASE_SUBMISSIONS_LINK, "").split("=")[1]
        )
        self.__hash = hashlib.sha1(self.__link.encode()).hexdigest()

        # TODO: should automatiically get ddataaa

    link = property(lambda self: self.__link)
    classID = property(lambda self: self.__classID)
    hashID = property(lambda self: self.__hash)
