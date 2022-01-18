from pandas import date_range, DataFrame, to_datetime
from datetime import timedelta


data_to_df = []

def quarter_period_create(df):
    periods = []
    third_fridays = date_range(df['Date'].iloc[len(df.index)-len(df.index)], df['Date'].iloc[len(df.index)-1], freq='WOM-2THU')
    starting_days_array = []
    ending_days_array = []
    for date in third_fridays:
        date = date + timedelta(days=1)
        if date.month == 3:
            starting_days_array.append(date)
        if date.month == 6:
            starting_days_array.append(date)
        if date.month == 9:
            starting_days_array.append(date)
        if date.month == 12:
            starting_days_array.append(date)
    for date in third_fridays:
        if date.month == 3:
            ending_days_array.append(date)
        if date.month == 6:
            ending_days_array.append(date)
        if date.month == 9:
            ending_days_array.append(date)
        if date.month == 12:
            ending_days_array.append(date)
    if len(starting_days_array) == len(ending_days_array):
        for index, date in enumerate(starting_days_array):
            ending_days_array_index = len(ending_days_array)-1
            if index < ending_days_array_index:
                periods.append(date)
                periods.append(ending_days_array[index+1])
            if index == ending_days_array_index:
                periods.append(date)
    return periods

def get_prices_of_period(df, startDay, endDay):
    df['Date'] = to_datetime(df['Date'])
    startDay = to_datetime(startDay)
    endDay = to_datetime(endDay)
    after_start_date = df["Date"] >= startDay
    before_end_date = df["Date"] <= endDay
    between_two_dates = after_start_date & before_end_date
    filtered_dates = df.loc[between_two_dates]
    highest_price = filtered_dates['High'].max()
    lowest_price = filtered_dates['Low'].min()
    opening_price = filtered_dates["Open"].iloc[len(filtered_dates.index)-len(filtered_dates.index)]
    closing_price = filtered_dates['Close'].iloc[len(filtered_dates.index)-1]
    return startDay, endDay, highest_price, lowest_price, opening_price, closing_price

def write_single_period(data):
    data_to_df.append([data[1], data[4], data[2], data[3], data[5], 0, 0])

def english_check_of_quarter(data):
    if sorted(data)[0] == 'Data':
        df = DataFrame(data, columns=['Data','Najwyzszy', 'Najnizszy','Otwarcie','Zamkniecie','Vol','OpenInt'])
        df = df.rename({'Najwyzszy':'High', 'Najnizszy':'Low', 'Otwarcie':'Open', 'Zamkniecie':'Close', 'Data':'Date',}, axis='columns')
    if sorted(data)[0] != 'Data':
        df = DataFrame(data, columns=['Date', 'High', 'Low', 'Open', 'Close', 'Vol', 'OpenInt'])
    return df

def quarter_saving(df, periods):
    for i in range(0, len(periods), 2):
        if i < len(periods)-1:
            s = to_datetime(periods[i].to_datetime64())
            e = to_datetime(periods[i+1].to_datetime64())
            s = s.date()
            e = e.date()
            data = get_prices_of_period(df, s, e)
            write_single_period(data)
        if i == len(periods) - 1:
            s = to_datetime(periods[i].to_datetime64())
            s = s.date()
            try:
                e = to_datetime(periods[i+1].to_datetime64())
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
                break
            except:
                max = df['Date'].max()
                e = max.to_datetime64()
                e = to_datetime(e)
                e = e.date()
                data = get_prices_of_period(df, s, e)
                write_single_period(data)
            finally:
                break
    return data_to_df
                                            