from datetime import datetime


class Notice:
    def __init__(
        self,
        title: str,
        author: str,
        authorType: str,
        rawBody: str,
        views: str,
        time: datetime,
        classID: int,
    ):
        self.__title = title
        self.__author = author
        self.__authorType = authorType
        self.__rawBody = rawBody
        self.__views = views
        self.__time = time
        self.__classID = classID
        self.__hashID = hash(str(self.__classID) + str(self.__title))

    @property
    def classID(self):
        return self.__classID

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def authorType(self):
        return self.__author

    @property
    def views(self):
        return self.__views

    @property
    def rawBody(self):
        return self.__rawBody

    @property
    def hashID(self):
        return self.__hashID

    @property
    def time(self):
        return self.__time

    @staticmethod
    def parseTime(timeStr: str) -> datetime:
        # TODO: parse time
        pass

    # TODO: parse rawBody
