"""
This module provides basic database operations for users.
"""

import sqlite3

def open_database(db_file="database.db"):
    """
    Opens a connection to the specified SQLite database.
    """
    connection = sqlite3.connect(db_file)
    return connection

def create_users_table(connection):
    """
    Creates the users table if it doesn't already exist.
    """
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        user_age INTEGER NOT NULL
    );
    '''
    connection.execute(create_table_sql)
    connection.commit()

def add_user(connection, username, user_age):
    """
    Inserts a new user into the users table.
    """
    insert_sql = "INSERT INTO users (username, user_age) VALUES (?, ?);"
    connection.execute(insert_sql, (username, user_age))
    connection.commit()

def fetch_all_users(connection):
    """
    Fetches all users from the users table.
    """
    select_sql = "SELECT * FROM users;"
    cursor = connection.execute(select_sql)
    return cursor.fetchall()

def modify_user_age(connection, user_id, updated_age):
    """
    Updates the age of the specified user.
    """
    update_sql = "UPDATE users SET user_age = ? WHERE user_id = ?;"
    connection.execute(update_sql, (updated_age, user_id))
    connection.commit()

def remove_user(connection, user_id):
    """
    Removes the specified user from the users table.
    """
    delete_sql = "DELETE FROM users WHERE user_id = ?;"
    connection.execute(delete_sql, (user_id,))
    connection.commit()
