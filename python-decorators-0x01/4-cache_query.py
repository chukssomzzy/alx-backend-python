#!/usr/bin/env python3

"""Cache queries"""


import functools
import sqlite3


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


query_cache = {}

"""your code goes here"""


def cache_query(func):
    """Cache query and result to query_cache"""
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        """Wrapper func"""

        if query in query_cache:
            return query_cache[query]
        query[query] = func(conn, query, *args, **kwargs)

        return query[query]

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)

    return cursor.fetchall()


# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
