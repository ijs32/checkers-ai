from sqlalchemy import text
import datetime as dt
from MySQLConn.mySQLdb import engine


class TrackGame():
    def __init__(self):
        ins_game_query = text("INSERT INTO `game` (winning_team, CREATE_DATE) VALUES ('IN PROGRESS', :now);")
    
        params={"now": dt.datetime.now()}
        with engine.connect() as conn:
            result = conn.execute(ins_game_query, params)
            conn.commit()
            if result.rowcount < 1:
                raise Exception("Insert failed")
            
        self.game_id = result.lastrowid


    def game_results_into_DB(self, winner):
        update_game_query = text("UPDATE `game` SET winning_team = :winner WHERE game_id = :game_id;")
        
        params={"winner": winner, "game_id": self.game_id}
        with engine.connect() as conn:
            result = conn.execute(update_game_query, params)
            conn.commit()
            if result.rowcount < 1:
                raise Exception("Insert failed")