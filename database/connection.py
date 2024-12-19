import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
driver = os.getenv("DB_DRIVER")
trusted_connection = os.getenv("DB_TRUSTED_CONNECTION")
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};"

try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
