import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import DECIMAL, Integer, String

db_uri = 'sqlite:////ramen_noodles/test.db'
engine = create_engine(db_uri)
ramen_noodles_df = pd.read_csv('ramen-ratings.csv')
connection = sqlite3.connect('ramen_noodles')
cursor = connection.cursor()
ramen_noodles_df.to_sql('ramen_noodles', engine, if_exists='replace', dtype={
    "review_number": Integer,
    "Brand": String,
    "Variety": String,
    "Style": String,
    "Country": String,
    "Stars": DECIMAL})
table_df = pd.read_sql_table(
    "ramen_noodles",
    con=engine
)