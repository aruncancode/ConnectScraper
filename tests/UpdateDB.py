import sqlite3


class UpdateDatabase():
    def __init__(self, file_name):
        self.conn = sqlite3.connect(file_name)
        self.c = self.conn.cursor()

    def add_user(self, first, last, username, password):

        self.first = first
        self.last = last
        self.username = username
        self.password = password

        with self.conn:
            self.c.execute(
                "INSERT INTO Users VALUES (:first, :last, :username, :password)",
                {
                    "first": self.first,
                    "last": self.last,
                    "username": self.username,
                    "password": self.password,
                },
            )

    def update_notices(self, dict):

        with self.conn:
            self.c.execute(
                "INSERT INTO Notices VALUES (:title, :body, :date, :person)",
                {
                    'title': dict['Title'],
                    'body': dict['Body'],
                    'date': dict['Date'],
                    'person': dict['Person']
                },
            )

    def update_submissions(self, dict):

        with self.conn:
            self.c.execute(
                "INSERT INTO Submissions VALUES (:title, :body, :date, :due_date, :class, :status, :person)",
                {
                    'title': dict['Title'],
                    'body': dict['Body'],
                    'date': dict['Date'],
                    'due_date': dict['Due Date'],
                    'class': dict['Class'],
                    'status': dict['Status'],
                    'person': dict['Person']
                },
            )

    # def update_marks(self, dict):

    #     with self.conn:
    #         self.c.execute(
    #             "INSERT INTO Submissions VALUES (:title, :body, :date, :due_date, :class, :status, :person)",
    #             {
    #                 'title': dict['Title'],
    #                 'body': dict['Body'],
    #                 'date': dict['Date'],
    #                 'due_date': dict['Due date'],
    #                 'class': dict['Class'],
    #                 'status': dict['Status'],
    #                 'person': dict['Person']
    #             },
    #         )

    # I DON"T KNOW HOW TO GET THE MARKS COZ OF THE DROP DOWN; DM ME
