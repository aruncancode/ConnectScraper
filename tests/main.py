import sqlite3

# from usersdb import User
# from connect_api import ConnectApi

conn = sqlite3.connect("user.db")
c = conn.cursor()


c.execute(
    """CREATE TABLE IF NOT EXISTS Users(
            first text,
            last text,
            username text,
            password text,
            )"""
)
