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
connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Timeout=30;"  # Increase the timeout to 30 seconds
    f"Trusted_Connection={trusted_connection};"
)


# Create connection
def get_sql_connection():
    return pyodbc.connect(connection_string)
