#!/usr/bin/env python3
"""Stream user data from a CSV file and insert into MySQL database"""

from itertools import islice
stream_users = __import__('0-stream_users').stream_users

# iterate over the generator function and print only the first 6 rows

for user in islice(stream_users(), 6):
    print(user)
