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

    def set_connection(self):
        print("OPEN CONNECTION")
        try:
            self.conn = psycopg2.connect(host="localhost", port=5432, dbname='postgres', user=self.user,
                                         password=self.password)
            self.cur = self.conn.cursor()
            auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            self.conn.set_isolation_level(auto_commit)
        except OperationalError:
            print("Connection Failed")
        if not self.is_table_exists():
            self._create_table()

    def close_connection(self):
        print("CLOSE CONNECTION")
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def _create_table(self):
        print("Create Table")
        self.cur.execute("""CREATE TABLE statistics
        (
            id SERIAL PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            points INTEGER NOT NULL,
            aristo_num INTEGER NOT NULL,
            cards_num INTEGER NOT NULL,
            games INTEGER NOT NULL,
            last_game TIMESTAMP
        );""")

    def check_if_player_exists(self, player_name):
        print("check_if_player_exists")
        self.cur.execute(f"SELECT name FROM {DBWorker.table_name} WHERE name = '{player_name}';")
        is_exists = self.cur.fetchone()
        return is_exists

    def read_data(self):
        self.cur.execute(
            f" SELECT ROW_NUMBER () OVER (ORDER BY points DESC, cards_num ASC), * FROM {DBWorker.table_name};")
        return self.cur.fetchall()

    def update_data(self, player) -> None:
        if not self.check_if_player_exists(player.name):
            print("INSERT")
            sql = f"INSERT INTO {DBWorker.table_name} (name, points, aristo_num, cards_num, games, last_game) VALUES (%s, %s, %s, %s, 1, CURRENT_TIMESTAMP);"
            self.cur.execute(sql, (
                player.name, player.points, player.all_stone_cards_num(), player.inventory.aristocratic_cards), )
        else:
            print("UPDATE")
            sql = f"UPDATE {DBWorker.table_name} SET points = points + %s, aristo_num = aristo_num + %s, cards_num = cards_num + %s, games = games + 1, last_game=CURRENT_TIMESTAMP WHERE name = %s;"
            self.cur.execute(sql, (
                player.points, player.all_stone_cards_num(), player.inventory.aristocratic_cards, player.name), )
        print("Update Table END")

    def reset_data(self):
        print("RESET STATISTICS")
        sql = f"TRUNCATE TABLE {DBWorker.table_name};"
        try:
            self.cur.execute(sql)
        except:
            print("CANT RESET")

    def is_table_exists(self):
        self.cur.execute(
            f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name ='{DBWorker.table_name}');")
        is_exists = self.cur.fetchone()[0]
        return is_exists
