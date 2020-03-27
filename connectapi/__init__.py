from requests import Session
from bs4 import BeautifulSoup as bs


class ConnectApi:
    def __init__(self, username: str, password: str):
        if not isinstance(username, str):
            raise TypeError("The username parameter must be a string.")
        if not isinstance(password, str):
            raise TypeError("The password parameter must be a string.")
        self.__username = username
        self.__password = password
        self.__s = None

    def login(self):
        with Session() as self.__s:
            site = self.__s.get("https://login.det.wa.edu.au/oam/server/obrareq.cgi?encquery%3DbPKvnLG4zJaQiON3%2Bp9vQkDuz5KpPGozevLjKgY76eSGfwKkjlotkknV5QNphwEFWqSgsivKQRpo9gNd8XvGj960VAV5X8UAGJMzW%2Fk6LoorLp2kg3y2ltk0PunbQh%2FLePCIXxtDBX3OX07vYS6soVgDPkJzNl%2Btc%2B1uwXqb8P3LaP3mJkwVx2XVCf3AI7N6Pc751JpS9ZWcD1O8pboDrNrLefBNSjS9arWkQ0Z8QcXHAHTn9rii3eBCMEzvdKj2RtLC%2FMiUQvdtM5TsBtreZlrwR50xkss3JkoKStatb9Q3h%2BeGoP3ZB5shYKx7%2B4owl7sN%2FAiLdqnI84y8lB9Z3%2B2wKBgifCRvdC20Aw11g%2Bpf%2BiezpmVDQgQJP3vUypjl%20agentid%3DCONNECT%20ver%3D1%20crmethod%3D2&ECID-Context=1.97289976909130380%3BkXhglXjE")
            bsContent = bs(site.content, "html.parser")
            hiddenStuff = {
                "site2pstoretoken": bsContent.find(
                    "input", {"name": "site2pstoretoken"}
                )["value"],
                "OAM_REQ": bsContent.find("input", {"name": "OAM_REQ"})[
                    "value"
                ],
                "request_id": bsContent.find("input", {"name": "request_id"})[
                    "value"
                ],
            }
            loginData = {
                "site2pstoretoken": hiddenStuff["site2pstoretoken"],
                "OAM_REQ": hiddenStuff["OAM_REQ"],
                "request_id": hiddenStuff["request_id"],
                "ssousername": self.__username,
                "password": self.__password,
                "acceptterms": "acceptterms",
                "submit": "Login",
            }
            self.__s.post(
                "https://login.det.wa.edu.au/oam/server/auth_cred_submit",
                loginData,
            )

    def getCustomPage(self, url: str, *, raw=False):
        if self.__s is None:
            raise Exception(
                "You must login to connect first using the login() method!"
            )
        if not isinstance(url, str):
            raise TypeError("The url parameter must be a string!")
        if not isinstance(raw, bool):
            raise TypeError("The raw parameter must be a bool!")

        page = self.__s.get(url)

        if raw:
            return page.text
        else:
            return bs(page.content, "html.parser")
