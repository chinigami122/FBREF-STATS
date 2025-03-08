import pandas as pd
import cryptography
from sqlalchemy import create_engine

# Load CSV file
df = pd.read_csv("new_matches1.csv")

# Convert date column to correct format
df["date"] = pd.to_datetime(df["date"], errors='coerce')

# Define MySQL connection (update with your credentials)
DATABASE_URL = "mysql+pymysql://root:s2004%40b22@localhost/football_stats1"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Load data into MySQL
df.to_sql("matches", con=engine, if_exists="replace", index=False)

print("Data successfully loaded into MySQL using SQLAlchemy.")
