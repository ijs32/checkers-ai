import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASSWD")
host = os.getenv("HOST")
cnx = mysql.connector.connect(user=user, password=password, host="localhost", database="localhost")