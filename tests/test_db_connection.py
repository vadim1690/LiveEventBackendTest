from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Replace with your actual database URL
DATABASE_URL = "mssql+pyodbc://api_user:api888@localhost/test_api_db?driver=ODBC+Driver+17+for+SQL+Server"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Database connection successful!")
except OperationalError as e:
    print("Database connection failed:", e)
