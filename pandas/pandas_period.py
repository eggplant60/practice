# -*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import numpy as np


# 1. DatetimeIndex の作成
dates = [dt.datetime(2014, 8, 1), 
         dt.datetime(2014, 8, 2)]
dti = pd.DatetimeIndex(dates)

np.random.seed(123456)

ts = pd.Series(
    data = np.random.randn(2),
    index = dates)

# print('1. DatetimeIndex')
# print(ts)


# 2. date_range の使用
dates = pd.date_range(
    start = '8/1/2014',
    periods = 10,
    freq = 'H')

# print('date_range')
# print(dates)


# 3. Period の使用
augYYYYMM = pd.Period(
    '2014-08',
    freq = 'M')

# print(augYYYYMM)
# print(augYYYYMM+1)

# print('start と end がある')
# print(augYYYYMM.start_time)
# print(augYYYYMM.end_time)


# 4. period_range の使用
periodRange = pd.period_range(
    start = '2016-10-20',
    end = '2016-11-10',
    freq = 'D'
)

# print('index のラベルが Period 型')
# print(periodRange)



# 5. 単位時間あたりの個数をカウント

df_event = pd.DataFrame(
    data = [1, 2, 3],
    index = pd.DatetimeIndex(['2016-10-20 20:19',
                              '2016-10-21 04:29',
                              '2016-10-22 23:22']))

time_failed = dt.datetime(2016, 10, 23)
time_from = time_failed - dt.timedelta(weeks=1)
time_to   = time_failed - dt.timedelta(hours=1)

dates = pd.date_range(
    end = time_to,
    periods = 168,
    freq = 'H')

# dummy
df_event.loc[time_from] = np.nan # nan はカウントしない
df_event.loc[time_to] = np.nan

#print(dates)
#print(df_event.groupby(0).groups)
df_count = df_event.groupby(pd.Grouper(freq='H', closed='right')).count()
df_max = df_event.groupby(pd.Grouper(freq='H', closed='right')).max()
df_max.fillna(0.0, inplace=True)
print(df_count)
print(df_max)


#df_event.resample('H').max()
