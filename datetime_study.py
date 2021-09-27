import pandas as pd

# ebola = pd.read_csv('./data/country_timeseries.csv')
# ebola['new_Date'] = pd.to_datetime(ebola['Date'])
# ebola['data_Year'] = ebola['new_Date'].dt.year
# ebola['data_Month'] = ebola['new_Date'].dt.month
# ebola['data_Day'] = ebola['new_Date'].dt.day
#
# print(ebola[['new_Date', 'data_Year', 'data_Month', 'data_Day']].dtypes)
# print(ebola[['new_Date', 'data_Year', 'data_Month', 'data_Day']])

# ts = pd.date_range(start='2021-07-01',  # 시작날짜
#                    end=None,  # 끝나는 날짜
#                    periods=12,  # 생성할 tiemstamp 수
#                    freq='MS',  # 시간주기(Month Start) 'W', 'D'
#                    tz='Asia/Seoul')  # 원하는 시간대(Time Zone)
# print(ts)

ts = pd.period_range(start='2021-07-01',
                     end=None,
                     periods=12,
                     freq='M')

data = ['3% 상승', '1% 상승', '3% 하락',
        '4% 상승', '2% 상승', '6% 상승',
        '3% 상승', '3% 상승', '3% 하락',
        '7% 하락', '1% 상승', '2% 하락']
sr = pd.Series(data=data, index=ts)
print(sr)

# print(ts)
