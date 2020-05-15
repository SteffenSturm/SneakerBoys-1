#Pandas importieren
import pandas as pd

#Pytrends importieren
from pytrends.request import TrendReq
pytrend = TrendReq()

#Google Trends Abfrage durchführen mit max. 5 verschiedenen Schuhnamen für einen bestimmten Zeitrahmen
pytrend.build_payload(kw_list=['Shoename1' , 'Shoename2' , 'Shoename3' , 'Shoename4' , 'Shoename4'], timeframe='today 3-m')
interest_over_time_df = pytrend.interest_over_time()

#Datei ausgeben
interest_over_time_df.to_csv('Search1.csv')

#Überflüssige erste (Datum) und letzte Spalte (isPartial) in Datei löschen
df = pd.read_csv('Search1.csv')
date = df.columns[0]
isPartial = df.columns[6]
df = df.drop([date, isPartial], axis=1)
df.to_csv('Search1-1.csv', index=False)

#Datei säubern (ausgegebenen Datensatz anhand ',' auf Spalten aufteilen)
raw_df = pd.read_csv('Search1-1.csv')
raw_df['Shoename1'] = raw_df['Shoename1'].str.split(',').str[0]
raw_df.to_csv('Search1-2.csv', index=False, sep=';', encoding='utf-8-sig')
