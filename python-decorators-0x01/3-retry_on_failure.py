#!/usr/bin/env python3
"""DB decorator that retry query incase of transient error"""

import functools
import sqlite3
import time


def with_db_connection(func):
    """ your code goes here"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function to manage database connection"""
        conn = sqlite3.connect("users.db")
        result = func(conn, *args, **kwargs)
        conn.close()

        return result

    return wrapper


""" your code goes here"""


def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            """Wraps a func and retry incase of transient error"""
            tries = 0

            while tries <= retries:
                try:
                    result = func(conn, *args, **kwargs)

                    return result
                except sqlite3.OperationalError as e:
                    if (tries == retries):
                        raise e
                    tries += 1
                    time.sleep(delay)

        return wrapper

    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    return cursor.fetchall()


users = fetch_users_with_retry()
print(users)
