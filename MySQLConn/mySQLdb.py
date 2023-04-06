import dotenv, os
from sqlalchemy import create_engine

dotenv.load_dotenv('./.env')

DB_USER = os.getenv("DB_USER")
DB_PASSWD = os.getenv("DB_PASSWD")

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWD}@localhost:3306/CheckersAI_test")
