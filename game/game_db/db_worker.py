import psycopg2
import datetime
from psycopg2 import OperationalError


class DBWorker:
    def __init__(self):
        pass

    def set_connection(self, db_name, user, password):
        conn = psycopg2.connect(host="localhost", port=5432, dbname=db_name, user=user,
                                password=password)
        self.__setattr__(f'conn_{user}', conn)
        self.__setattr__(f'cur_{user}', conn.cursor())
        auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        conn.set_isolation_level(auto_commit)

    def create_db(self):
        print("Create DB")
        cursor = self.__getattribute__(f"cur_{self.user}")
        cursor.execute("CREATE DATABASE splendor_db;")

    def create_table(self):
        print("Create Table")
        print(self.user)
        cursor = self.__getattribute__(f"cur_{self.user}")
        cursor.execute("""CREATE TABLE best_scores
        (
            best_scores_id SERIAL PRIMARY KEY,
            rank INTEGER NOT NULL,
            name VARCHAR(10) NOT NULL,
            points INTEGER NOT NULL,
            aristo_num INTEGER NOT NULL,
            cards_num INTEGER NOT NULL,
            last_game TIMESTAMP NOT NULL
        );""")

    def read_data(self):
        print("Read Table")
        cursor = self.__getattribute__(f"cur_{self.user}")
        cursor.execute("""SELECT * FROM best_scores;""")
        print("DISPLAY DATA")
        print(cursor.fetchall())
        for row in cursor.fetchall():
            print(row)

    def update_data(self, data: list) -> None:
        print("Update Table")
        cursor = self.__getattribute__(f"cur_{self.user}")
        # lista = [(row, 'Mario', row, row, row, '2017-11-04T05:05:18.161681Z') for row in range(1,50)] properly example of data
        for row in data:
            sql = "INSERT INTO best_scores (rank, name, points, aristo_num, cards_num, last_game) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, row)
        print("Update Table END")

    def delete_data(self):
        pass

    def __enter__(self):
        print("ENTER")
        try:
            print("Try to connect to splendor_db")
            self.__setattr__('user', 'postgres')
            self.set_connection("splendor_db", self.user, "admin")
            print("Connected...")
        except OperationalError:
            print("Connection Failed")
            print("Need to create splendor_db")
            self.__setattr__('user', 'postgres')
            self.set_connection("postgres", self.user, "admin")
            self.create_db()
            self.set_connection("splendor_db", self.user, "admin")
            print("Connected...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")
        conn = self.__getattribute__(f"conn_{self.user}")
        cursor = self.__getattribute__(f"cur_{self.user}")
        conn.commit()
        cursor.close()
        conn.close()
        self.__delattr__(f"conn_{self.user}")
        self.__delattr__(f"cur_{self.user}")


my_db = DBWorker()

with my_db:
    try:
        data = []
        my_db.update_data(data)
    except:
        pass
    try:
        my_db.read_data()
    except:
        my_db.create_table()
        my_db.read_data()
