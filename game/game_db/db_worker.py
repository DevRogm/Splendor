import psycopg2
import datetime
from psycopg2 import OperationalError


class DBWorker:
    table_name = 'statistics'
    def __init__(self):
        self.user = 'postgres'
        self.password = 'admin'
        self.conn = None
        self.cur = None

    def _set_connection(self, db_name, user, password):
        print("OPEN CONNECTION")
        self.conn = psycopg2.connect(host="localhost", port=5432, dbname=db_name, user=user,
                                     password=password)
        self.cur = self.conn.cursor()
        auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        self.conn.set_isolation_level(auto_commit)
        print("OPENED CONNECTION")

    def _close_connection(self):
        print("CLOSE CONNECTION")
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        print("CLOSED CONNECTION")

    def _create_table(self):
        print("Create Table")
        self.cur.execute("""CREATE TABLE statistics
        (
            id SERIAL PRIMARY KEY,
            rank INTEGER NOT NULL,
            name VARCHAR(10) NOT NULL,
            points INTEGER NOT NULL DEFAULT 0,
            aristo_num INTEGER NOT NULL DEFAULT 0,
            cards_num INTEGER NOT NULL DEFAULT 0,
            last_game TIMESTAMP
        );""")

    def read_data(self):
        print("Read Table")
        self.cur.execute(f"SELECT * FROM {DBWorker.table_name};")
        print("DISPLAY DATA")
        for row in self.cur.fetchall():
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

    def is_table_exists(self, table_name):
        self.cur.execute(
            f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name ='{table_name}');")
        is_exists = self.cur.fetchall()[0][0]
        return is_exists

    def __enter__(self):
        try:
            print("Try to connect to postgres db")
            self._set_connection("postgres", self.user, self.password)
            print("Connected...")
            if not self.is_table_exists(DBWorker.table_name):
                self._create_table()
        except OperationalError:
            print("Connection Failed")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_connection()


# my_db = DBWorker()
#
# with my_db:
#     my_db.read_data()
