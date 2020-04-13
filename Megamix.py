# Pandas importieren
import pandas as pd

# Pytrends importieren
from pytrends.request import TrendReq

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['Vans Comfycush Slip-On Half Big Checker', 'Jordan Delta SP Sail', 'Jordan 6 Retro DMP (2020)', 'Nike KD 13 Chill', 'Nike Kyrie 6 USA'])

# Interest Over Time abfragen und in .csv Datei ausgeben
interest_over_time_df = pytrend.interest_over_time()
interest_over_time_df.to_csv('time.csv')

# Ausgegebene .csv Datei lesen und Ergebnissen anhand der , eigene Spalten zuweisen
raw_df = pd.read_csv("time.csv")
raw_df
raw_df.describe()
raw_df.tail()
raw_df.head()
raw_df.isna().sum()
raw_df['date'] = raw_df['date'].str.split(',').str[0]
raw_df
raw_df.to_csv('timetidy.csv', index=False, sep=';', encoding='utf-8-sig')
