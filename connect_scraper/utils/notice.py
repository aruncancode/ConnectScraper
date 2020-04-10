from datetime import datetime
from .. import BASE_ANNOUNCMENT_LINK


class Notice:
    def __init__(
        self,
        title: str,
        author: str,
        authorType: str,
        rawBody: str,
        views: str,
        time: datetime,
        link: str,
    ):
        self.__title = title
        self.__author = author
        self.__authorType = authorType
        self.__rawBody = rawBody
        self.__views = views
        self.__time = time
        self.__link = link
        self.__classID = int(
            self.__link.replace(BASE_ANNOUNCMENT_LINK, "").split("&")[0]
        )
        self.__id = int(
            self.__link.replace(
                BASE_ANNOUNCMENT_LINK + str(self.__classID) + "&viewNotice=", ""
            )
        )

    @staticmethod
    def parseTime(timeStr: str) -> datetime:
        # TODO: parse time
        pass

    # TODO: parse rawBody
