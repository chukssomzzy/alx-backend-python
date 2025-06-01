#!/usr/bin/env python3
"""Defines a transactional decorator to make sure database operations are a acidic"""
import sqlite3
import functools

"""your code goes here"""


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


def transactional(func):
    """Decorator to handle db transactions"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        """Wrapper function to manager db transactions"""
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()

            return result
        except Exception as e:
            conn.rollback()

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?",
                   (new_email, user_id))


# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
