import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWD")
host = os.getenv("HOST")
conn = mysql.connector.connect(user=user, password=password, host=host, database="CheckersAI")