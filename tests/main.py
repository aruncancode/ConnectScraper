from UpdateDB import UpdateDatabase
from connect_api import ConnectApi
import sqlite3, time, json

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("SELECT username, password FROM Users")
result_set = c.fetchall()
c.close()

for username, password in result_set:
    connect = ConnectApi(username, password)
    connect.login()
    time.sleep(2)

    notices = connect.get_notices()
    submissions = connect.get_submissions()

    db = UpdateDatabase('users.db')
    db.update_notices(notices)
    time.sleep(1)
    db.update_submissions(submissions)

# db = UpdateDatabase('users.db')
# db.add_user('INSERT NAME', 'LAST NAME', "USERNAME (CONNECT)" , "PASSWORD")
'''
setup first before running:
    1. Download SQLbrowser
    2. Create a file called "users.db" in the MAIN  directory.
    2. comment out all code from 4-23
    3. uncomment the add person command lines, and run the code.
    4. now you should be able to run the loop which basically simulates periodic update to the db
'''