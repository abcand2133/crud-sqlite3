import sqlite3

class DBConnection:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def commit_and_close(self):
        self.connection.commit()
        self.connection.close()


class TableCreator(DBConnection):
    def __init__(self, db_name: str):
        super().__init__(db_name)

    def create_users_table(self) -> None:
        sql = """
            DROP TABLE IF EXISTS users;
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE
            );
        """
        self.cursor.executescript(sql)

    def create_todos_table(self):
        sql = """
        DROP TABLE IF EXISTS todos;
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            description TEXT ,
            created_at TEXT,
            user_id INTEGER REFERENCES users(id)
            );   
        """
        self.cursor.executescript(sql)


# creator = TableCreator('todos.db')
# creator.create_users_table()
# creator.create_todos_table()
# creator.commit_and_close()
