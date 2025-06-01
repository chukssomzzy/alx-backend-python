#!/usr/bin/env python3

"""Reusable class based context manager"""

import sqlite3


class ExecuteQuery:
    """Manages connection and execute query"""

    def __init__(self, query, params):
        """Initialize a connection"""
        self.conn = sqlite3.connect("users.db")
        self.cur = self.conn.cursor()
        self.query = query
        self.params = (params,)

    def __enter__(self):
        """Returns the result of the execution of the query"""
        self.cur.execute(self.query, self.params)

        return self.cur.fetchall()

    def __exit__(self, type, value, traceback):
        self.cur.close()
        self.conn.close()

        return True


with ExecuteQuery("SELECT * FROM users WHERE age > ?", 25) as result:
    print(result)
