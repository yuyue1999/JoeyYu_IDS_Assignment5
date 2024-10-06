import pytest
import main

@pytest.fixture
def setup_db():
    conn = main.open_database(":memory:")
    main.create_users_table(conn)
    yield conn
    conn.close()

def test_add_user(setup_db):
    main.add_user(setup_db, "Joey", 24)
    users = main.fetch_all_users(setup_db)
    assert len(users) == 1
    assert users[0][1] == "Joey"
    assert users[0][2] == 24

def test_modify_user_age(setup_db):
    main.add_user(setup_db, "Joey", 24)
    main.modify_user_age(setup_db, 1, 18)
    users = main.fetch_all_users(setup_db)
    assert users[0][2] == 18

def test_remove_user(setup_db):
    main.add_user(setup_db, "Joey", 24)
    main.remove_user(setup_db, 1)
    users = main.fetch_all_users(setup_db)
    assert len(users) == 0
