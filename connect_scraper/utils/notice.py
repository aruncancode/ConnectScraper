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

    classID = property(lambda self: self.__classID)
    title = property(lambda self: self.__title)
    author = property(lambda self: self.__author)
    authorType = property(lambda self: self.__authorType)
    views = property(lambda self: self.__views)
    rawBody = property(lambda self: self.__rawBody)
    hashID = property(lambda self: self.__hashID)
    time = property(lambda self: self.__time)

    @staticmethod
    def parseTime(timeStr: str) -> datetime:
        # TODO: parse time
        pass

    # TODO: parse rawBody
