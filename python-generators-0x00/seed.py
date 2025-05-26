#!/usr/bin/env python3

"""Seed mysql database with initial data"""
from typing import List, Tuple
import mysql.connector
from dotenv import load_dotenv
from os import environ
import csv
from uuid import uuid4

load_dotenv()

CREATE_DATABASE_QUERY = """CREATE DATABASE IF NOT EXISTS ALX_prodev"""
CREATE_TABLE_QUERY = (
    "CREATE TABLE IF NOT EXISTS user_data ("
    "user_id VARCHAR(36) NOT NULL PRIMARY KEY,"
    "name VARCHAR(255) NOT NULL,"
    "email VARCHAR(255) NOT NULL UNIQUE,"
    "age INT NOT NULL)")


def connect_db():
    """
        Mysql db connector
    """
    try:
        return mysql.connector.connect(
            host=environ.get("MYSQL_HOST", "localhost"),
            user=environ.get("MYSQL_USER", "root"),
            password=environ.get("MYSQL_PASSWORD", "mysql_root_pwd"),
            database=environ.get("MYSQL_DATABASE", "mysql_db"),
        )
    except mysql.connector.Error:
        return None


def create_database(connection: mysql.connector.connection.MySQLConnection):
    """
        Create database if it does not exist
    """
    with connection.cursor() as cursor:
        cursor.execute(CREATE_DATABASE_QUERY)
        connection.commit()


def connect_to_prodev():
    """Connect to the ALX_prodev database"""
    connection = connect_db()
    if connection is None:
        return None
    with connection.cursor() as cursor:
        cursor.execute("USE ALX_prodev")
        connection.commit()
    return connection


def create_table(connection: mysql.connector.connection.MySQLConnection):
    """
        Create table if it does not exist
    """
    with connection.cursor() as cursor:
        cursor.execute(CREATE_TABLE_QUERY)
        connection.commit()


def insert_data(connection: mysql.connector.connection.MySQLConnection, user_data: str):
    """
        Insert data into the user_data table
        Args:
            connection: MySQL connection object
            user_data: Path to the file containing user data in csv format
    """
    insert_query = """
        INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
    """
    with connection.cursor() as cursor:
        data: List[Tuple[str, str, str, int]] = []
        with open(user_data, 'r') as f:
            data = [(str(uuid4()), user[0], user[1], int(user[2]) if user[2].isdigit() else 0)
                    for user in csv.reader(f)][1:]
        cursor.executemany(insert_query, data)
        connection.commit()
