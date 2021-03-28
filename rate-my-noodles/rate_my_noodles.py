import sqlite3
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import DECIMAL, Integer, String

db_uri = 'sqlite:///ramen_noodles.db'
engine = create_engine(db_uri)
ramen_noodles_df = pd.read_csv('ramen-ratings.csv')
ramen_noodles_df = ramen_noodles_df.drop('Top Ten', 1)
ramen_noodles_df = ramen_noodles_df.drop('Review #', 1)
ramen_noodles_df = ramen_noodles_df.drop('Style', 1)
ramen_noodles_df = ramen_noodles_df.drop('Country', 1)
ramen_noodles_df = ramen_noodles_df.replace('Unrated', np.NaN)
ramen_noodles_df.to_sql('ramen_noodles', engine, if_exists='replace', dtype={
    "review_number": Integer,
    "Brand": String,
    "Variety": String,
    "Stars": DECIMAL})
table_df = pd.read_sql_table(
    "ramen_noodles",
    con=engine
)
print("Brand?")
brand = input()
print("Variety?")
variety = input()
sql = text('select Stars from ramen_noodles where Brand=:mv and Variety=:ml')
Session = sessionmaker(bind=engine)
session = Session()
rating = session.execute(sql, {'mv': brand, 'ml': variety})
result = [row[0] for row in rating]

print(str(result[0]) + ' out of 5 stars')
if float(result[0]) >= 4:
    print('Mmmmm delicious')
elif float(result[0]) <= 1.5:
    print('Don\'t eat these yo')
else:
    print('Worth trying')



