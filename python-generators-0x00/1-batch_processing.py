#!/usr/bin/env python3

"""Filter and batch read user data from MYSQL database"""

stream_users = __import__('0-stream_users').stream_users


def batch_processing(batch_size: int = 5):
    """Batch process user  data from the database
        filtering out users with age less than 25
    Args:
        batch_size (int): Number of users to process in each batch
    """
    batch = []
    for user in stream_users():
        batch.append(user)
        if len(batch) == batch_size:
            for u in batch:
                if u['age'] > 25:
                    print(u)
            batch = []
    for u in batch:
        if u['age'] > 25:
            print(u)
