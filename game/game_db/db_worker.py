import psycopg2
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

    def create_db_user(self, user, password):
        print("Create User")
        cursor = self.__getattribute__(f"cur_{self.user}")
        cursor.execute(f"CREATE USER {user} WITH ENCRYPTED PASSWORD '{password}';")
        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE splendor_db to {user};")

    def create_db(self):
        print("Create DB")
        cursor = self.__getattribute__(f"cur_{self.user}")
        cursor.execute("CREATE DATABASE splendor_db;")

    def read_db(self):
        pass

    def update_db(self):
        pass

    def delete_db(self):
        pass

    def __enter__(self):
        print("ENTER")
        try:
            print("Try to connect to splendor_db")
            self.__setattr__('user', 'splendor_user')
            self.set_connection("splendor_db", self.user, "splendix")
            print("Connected...")
        except OperationalError:
            print("Connection Failed")
            print("Need to create splendor_db")
            self.__setattr__('user', 'postgres')
            self.set_connection("postgres", self.user, "admin")
            self.create_db()
            self.create_db_user('splendor_user', 'splendix')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")
        conn = self.__getattribute__(f"conn_{self.user}")
        cursor = self.__getattribute__(f"cur_{self.user}")
        conn.commit()
        cursor.close()
        conn.close()
        self.__delattr__(f"cur_{self.user}")
