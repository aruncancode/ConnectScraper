import sqlite3


# class User:
#     def __init__(self, first, last, username, password):
#         self.first = first
#         self.last = last
#         self.username = username
#         self.password = password
#         self.db = {
#             "Name": (first, last),
#             "Username": username,
#             "Password": password,
#             "Notices": {"Title": [], "Date": [], "Body": []},
#             "Marks": {"Title": [], "Class": [], "Date": [], "Mark": []},
#             "Submissions": {
#                 "Title": [],
#                 "Date": [],
#                 "Body": [],
#                 "Due Date": [],
#                 "Class": [],
#             }
#         }


#     def notices(self, title, body, date):
#         self.db["Notices"]["Title"].append(title)
#         self.db["Notices"]["Date"].append(date)
#         self.db["Notices"]["Body"].append(body)

#         return self.db["Notices"]["Title"][-1]

#     def submissions(self, title, body, date, subject, due_date):
#         self.db["Submissions"]["Title"].append(title)
#         self.db["Submissions"]["Date"].append(date)
#         self.db["Submissions"]["Body"].append(body)
#         self.db["Submissions"]["Due Date"].append(due_date)
#         self.db["Submissions"]["Class"].append(subject)

#     def marks(self, title, date, mark, subject):
#         self.db["Marks"]["Title"].append(title)
#         self.db["Marks"]["Date"].append(date)
#         self.db["Marks"]["Class"].append(subject)
#         self.db["Marks"]["Mark"].append(mark)

#         return self.db["Mark"]


class User:

    conn = sqlite3.connect("user.db")
    c = conn.cursor()

    def __init__(self, first, last, username, password):
        self.first = first
        self.last = last
        self.username = username
        self.password = password

        c.execute(
            "INSERT INTO Users VALUES (:first, :last, :username:, :password)",
            {
                "first": self.first,
                "last": self.last,
                "username": self.username,
                "password": self.password,
            },
        )
