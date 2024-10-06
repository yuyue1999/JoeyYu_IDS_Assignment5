"""
This module contains unit tests for the database operations in main.py.
"""

import pytest
import main

def test_add_user():
    """
    Test adding a user to the database.
    """
    db_conn = main.open_database(":memory:")
    main.create_users_table(db_conn)
    main.add_user(db_conn, "Joey", 24)
    users = main.fetch_all_users(db_conn)
    db_conn.close()
    assert len(users) == 1
    assert users[0][1] == "Joey"
    assert users[0][2] == 24

def test_modify_user_age():
    """
    Test modifying a user's age.
    """
    db_conn = main.open_database(":memory:")
    main.create_users_table(db_conn)
    main.add_user(db_conn, "Joey", 24)
    main.modify_user_age(db_conn, 1, 18)
    users = main.fetch_all_users(db_conn)
    db_conn.close()
    assert users[0][2] == 18

def test_remove_user():
    """
    Test removing a user from the database.
    """
    db_conn = main.open_database(":memory:")
    main.create_users_table(db_conn)
    main.add_user(db_conn, "Joey", 24)
    main.remove_user(db_conn, 1)
    users = main.fetch_all_users(db_conn)
    db_conn.close()
    assert len(users) == 0
