from UpdateDB import UpdateDatabase
from connect_scraper import ConnectScraper
import sqlite3, time, json

conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("SELECT username, password FROM Users")
result_set = c.fetchall()
c.close()

for username, password in result_set:
    connect = ConnectScraper(username, password, headless=True)
    connect.login()
    time.sleep(2)

    notices = connect.get_notices()
    submissions = connect.get_submissions()

    db = UpdateDatabase("users.db")
    time.sleep(1)
    db.update_notices(notices)
    time.sleep(1)
    db.update_submissions(submissions)

# db = UpdateDatabase('users.db')
# db.add_user('INSERT NAME', 'LAST NAME', "USERNAME (CONNECT)" , "PASSWORD")
