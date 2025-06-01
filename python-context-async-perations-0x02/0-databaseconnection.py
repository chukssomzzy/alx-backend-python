#!/usr/bin/env python3

"""Context Manager to handle db connection"""

import sqlite3


class DatabaseConnection:
    def __init__(self, db):
        """Initialize db connection"""
        self.conn = sqlite3.connect(db)

    def __enter__(self):
        """Returns the db connection object"""

        return self.conn

    def __exit__(self, type, value, traceback):
        """Handles the exist of the db connection"""
        self.conn.close

        return True


with DatabaseConnection("user.db") as conn:
    cur = conn.cursor()
    users = cur.execute("SELECT * FROM users")
    print(users)
