import pandas as pd

def  extract_feats(data, holidays):
    _, week, weekday = list(zip(*data.reset_index()['Дата и время'].apply(pd.Timestamp.isocalendar)))
    data['weekday'] = weekday
    data['week'] = week
    data['hour'] = data.reset_index()['Дата и время'].dt.hour.values
    data['yearday'] = data.reset_index()['Дата и время'].dt.dayofyear.values
    data['month'] = data.reset_index()['Дата и время'].dt.month.values
    # data['weekday'] = data.reset_index()['Дата и время'].dt.weekday.values
    # data['week'] = data.reset_index()['Дата и время'].dt.week.values
    data['holidays'] = data.reset_index()['Дата и время'].dt.date.isin(holidays.keys()).astype(int).values
    return data