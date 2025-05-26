#!/usr/bin/env python3

"""Filter and batch read user data from MYSQL database"""

seed = __import__('seed')

SELECT_USER_QUERY = "SELECT * FROM user_data"


def stream_users_in_batches(batch_size: int = 5):
    """Stream user data from the database"""
    connection = seed.connect_to_prodev()

    if connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_USER_QUERY)
            rows = cursor.fetchmany(batch_size)
            while rows:
                for user in rows:
                    yield {"user_id": user[0], 'name': user[1], 'email': user[2], 'age': int(user[3])}
                rows = cursor.fetchmany(batch_size)
        connection.close()


def batch_processing(batch_size: int = 5):
    """Batch process user  data from the database
        filtering out users with age less than 25
    Args:
        batch_size (int): Number of users to process in each batch
    """
    for user in stream_users_in_batches(batch_size):
        if user['age'] > 25:
            print(user)
    return None
