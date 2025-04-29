-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    return ( bikes
            .groupby('bike_number', as_index=False)['end_time']
            .max()
            .sort_values(by='end_time', ascending=False)
           )

