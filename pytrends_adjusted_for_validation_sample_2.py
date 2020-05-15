#Pandas importieren
import pandas as pd

#Pytrends importieren
from pytrends.request import TrendReq
pytrend = TrendReq()

#Google Trends Abfrage durchführen mit max. 5 verschiedenen Schuhnamen für einen bestimmten Zeitrahmen
pytrend.build_payload(kw_list=['adidas Yeezy 700 V3 Alvah' , 'adidas Yeezy 500 High Slate' , 'adidas Yeezy 500 Stone Yeezy' , 'adidas Yeezy Boost 350 V2 Desert Savage' , 'adidas Yeezy 500 Salt'], timeframe='2018-11-01 2020-04-26')
interest_over_time_df = pytrend.interest_over_time()

#Datei ausgeben
interest_over_time_df.to_csv('time1.csv')
