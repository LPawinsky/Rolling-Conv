import pandas as pd
import datetime as dt

def cols_rename(df):
    df = df[['<DATE>','<OPEN>','<HIGH>','<LOW>','<CLOSE>','<VOL>','<OPENINT>']]
    if sorted(df)[1] == '<DATE>':
        df.rename(columns={'<DATE>':'Date','<OPEN>':'Open','<HIGH>':'High','<LOW>':'Low','<CLOSE>':'Close','<VOL>':'Vol','<OPENINT>':'OpenInt'}, inplace=True)
    return df

def english_check(df):
    df['Vol'] = 0
    df['OpenInt'] = 0
    if sorted(df)[0] == 'Data':
        df[['Data','Otwarcie','Najwyzszy','Najnizszy','Zamkniecie','Vol','OpenInt']]
        df.rename(columns={'Data':'Date','Otwarcie':'Open','Najwyzszy':'High','Najnizszy':'Low','Zamkniecie':'Close'}, inplace=True)
    return df

def date_transform(df):
    df['Date'] = pd.to_datetime(df['Date'].astype(str), format='%Y-%m-%d')
    df['Date'] = df['Date'].dt.date
    return df
    

def normalize(path, case):
    type = case[1:]
    if type == 'txt':
        data = pd.read_csv(path)
        df = pd.DataFrame(data, columns=['<TICKER>','<PER>','<DATE>','<OPEN>','<HIGH>','<LOW>','<CLOSE>','<VOL>','<OPENINT>'])
        renamed = cols_rename(df)
        return renamed
    if type == 'csv':
        df = pd.read_csv(path)
        renamed = english_check(df)
        return renamed
