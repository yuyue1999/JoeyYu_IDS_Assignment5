import pytest
import main

@pytest.fixture
def db_connection():
    conn = main.open_database(":memory:")
    main.create_users_table(conn)
    yield conn
    conn.close()

def test_add_user(db_connection):
    main.add_user(db_connection, "Joey", 24)
    users = main.fetch_all_users(db_connection)
    assert len(users) == 1
    assert users[0][1] == "Joey"
    assert users[0][2] == 24

def test_modify_user_age(db_connection):
    main.add_user(db_connection, "Joey", 24)
    main.modify_user_age(db_connection, 1, 18)
    users = main.fetch_all_users(db_connection)
    assert users[0][2] == 18

def test_remove_user(db_connection):
    main.add_user(db_connection, "Joey", 24)
    main.remove_user(db_connection, 1)
    users = main.fetch_all_users(db_connection)
    assert len(users) == 0
