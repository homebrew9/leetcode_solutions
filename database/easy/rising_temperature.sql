-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    weather['prev_date'] = weather.shift(1)['recordDate']
    weather['prev_temp'] = weather.shift(1)['temperature']
    weather['is_higher'] = ( np.where(
                               ((weather['recordDate'] - weather['prev_date'])/np.timedelta64(1,'D') == 1)
                               &
                               (weather['temperature'] > weather['prev_temp']), 'Y', 'N'
                             )
                           )
    return weather[weather['is_higher'] == 'Y'][['id']]

