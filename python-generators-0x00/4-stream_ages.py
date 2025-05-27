#!/usr/bin/env python3

"""Get average age stream"""

seed = __import__("seed")


def stream_user_ages():
    """Age generator"""
    cnx = seed.connect_to_prodev()
    with cnx.cursor() as c:
        user = None
        offset = 0
        page_size = 1
        while True:
            c.execute(
                f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
            user = c.fetchall()
            if not user:
                break
            yield user[0][3]

            offset += page_size


def calculate_avg_age():
    avg_age = 0
    num_age = 0
    for age in stream_user_ages():
        avg_age += int(age)
        num_age += 1
    print(f"Average age of users: {avg_age / num_age if num_age else 1}")


if __name__ == "__main__":
    calculate_avg_age()
