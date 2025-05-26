#!/usr/bin/env python3

"""Stream user data from database"""

seed = __import__('seed')

SELECT_USER_QUERY = "SELECT * FROM user_data"


def stream_users():
    """Stream user data from the database"""
    connection = seed.connect_to_prodev()

    if connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_USER_QUERY)
            for user in cursor.fetchall():
                yield {"user_id": user[0], 'name': user[1], 'email': user[2], 'age': int(user[3])}
        connection.close()
