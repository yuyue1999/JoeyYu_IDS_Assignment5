import sqlite3

def open_database(db_file="database.db"):
    connection = sqlite3.connect(db_file)
    return connection

def create_users_table(connection):
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
    insert_sql = "INSERT INTO users (username, user_age) VALUES (?, ?);"
    connection.execute(insert_sql, (username, user_age))
    connection.commit()

def fetch_all_users(connection):
    select_sql = "SELECT * FROM users;"
    cursor = connection.execute(select_sql)
    return cursor.fetchall()

def modify_user_age(connection, user_id, updated_age):
    update_sql = "UPDATE users SET user_age = ? WHERE user_id = ?;"
    connection.execute(update_sql, (updated_age, user_id))
    connection.commit()

def remove_user(connection, user_id):
    delete_sql = "DELETE FROM users WHERE user_id = ?;"
    connection.execute(delete_sql, (user_id,))
    connection.commit()

def run_app():
    db_conn = open_database()
    create_users_table(db_conn)

    add_user(db_conn, "Tom", 18)
    add_user(db_conn, "Jerry", 20)

    print("Users after adding:")
    all_users = fetch_all_users(db_conn)
    for user in all_users:
        print(user)

    modify_user_age(db_conn, 2, 21)
    print("\nUsers after modifying age:")
    all_users = fetch_all_users(db_conn)
    for user in all_users:
        print(user)

    remove_user(db_conn, 2)
    print("\nUsers after removing:")
    all_users = fetch_all_users(db_conn)
    for user in all_users:
        print(user)

    db_conn.close()

if __name__ == "__main__":
    run_app()
