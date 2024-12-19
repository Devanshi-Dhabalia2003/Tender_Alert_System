import pyodbc
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# SQL Server Connection Setup
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
driver = os.getenv("DB_DRIVER")
trusted_connection = os.getenv("DB_TRUSTED_CONNECTION")
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

# Create connection
def get_sql_connection():
    return pyodbc.connect(connection_string)
