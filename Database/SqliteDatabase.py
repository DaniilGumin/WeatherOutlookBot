import os
import sqlite3
from typing import Optional

from Database.IDatabase import IDatabase


class SqliteDatabase(IDatabase):
    def __init__(self):
        self.conn = sqlite3.connect(os.environ.get('DATABASE_NAME'), check_same_thread=False,
                                    detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.database_config()

    def database_config(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS city(
                user_id INT PRIMARY KEY,
                city VARCHAR(50))
                """)
        self.conn.commit()

    def add_player(self, player_id: int, name: str, player_birthdate: str, foot: str, height: int,
                   season_id: int, team_id: int) -> None:
        self.cur.execute("""INSERT OR REPLACE INTO players (player_id, name, birthdate, foot, height) 
                   VALUES(?, ?, ?, ?, ?);""", [player_id, name, player_birthdate, foot, height])
        self.conn.commit()
        self.cur.execute("""INSERT OR IGNORE INTO table_bundle (season_id, player_id, team_id) 
                           VALUES(?, ?, ?);""", [season_id, player_id, team_id])
        self.conn.commit()

    def save_last_city_for_user(self, user_id: int, city: str) -> None:
        self.cur.execute("""INSERT OR REPLACE INTO city(user_id, city) 
                                   VALUES(?, ?);""", [user_id, city])
        self.conn.commit()

    def get_last_city_by_user_id(self, user_id: int) -> Optional[str]:
        self.cur.execute("""SELECT * FROM city WHERE user_id = ?;""", [user_id])
        city = self.cur.fetchall()
        if city is not None:
            return city[0]
        return None
