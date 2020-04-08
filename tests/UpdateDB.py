import sqlite3


class UpdateDatabase:
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
                "SELECT * FROM Notices WHERE (title=? AND body=? AND date=? AND person=? AND class=?)",
                (
                    dict["Title"],
                    dict["Body"],
                    dict["Date"],
                    dict["Person"],
                    dict["Subject"],
                ),
            )
            entry = self.c.fetchone()

            if entry is None:
                self.c.execute(
                    "INSERT INTO Notices VALUES (:title, :body, :date, :person, :class)",
                    {
                        "title": dict["Title"],
                        "body": dict["Body"],
                        "date": dict["Date"],
                        "person": dict["Person"],
                        "class": dict["Subject"],
                    },
                )

    def update_submissions(self, dict):

        with self.conn:

            self.c.execute(
                "SELECT * FROM Submissions WHERE (title=? AND body=? AND date=? AND due_date=? AND class=? AND status=? AND person=?)",
                (
                    dict["Title"],
                    dict["Body"],
                    dict["Date"],
                    dict["Due Date"],
                    dict["Class"],
                    dict["Status"],
                    dict["Person"],
                ),
            )
            entry = self.c.fetchone()

            if entry is None:

                self.c.execute(
                    "INSERT INTO Submissions VALUES (:title, :body, :date, :due_date, :class, :status, :person)",
                    {
                        "title": dict["Title"],
                        "body": dict["Body"],
                        "date": dict["Date"],
                        "due_date": dict["Due Date"],
                        "class": dict["Class"],
                        "status": dict["Status"],
                        "person": dict["Person"],
                    },
                )

    # def update_marks(self, dict):

    #     with self.conn:
    #         self.c.execute(
    #             "INSERT INTO Submissions VALUES (:title, :raw_mark, :weighted_mark, :percentage, :subject, :date, :person)",
    #             {
    #                 'title': dict['Title'],
    #                 'raw_mark': dict['Raw_mark'],
    #                 'weighted_mark': dict['Weighted_mark'],
    #                 'percentage': dict['Percentage'],
    #                 'subject': dict['Subject'],
    #                 'date': dict['Date'],
    #                 'person': dict['Person']
    #             },
    #         )
