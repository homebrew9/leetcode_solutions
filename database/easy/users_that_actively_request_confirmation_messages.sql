-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Sort by user_id and time_stamp first, so that shift() works correctly
    confirmations = confirmations.sort_values(by=['user_id','time_stamp'])
    
    # Add the lag value partitioned by user_id
    confirmations['lag'] = confirmations.groupby('user_id',as_index=False)['time_stamp'].shift(1)
    
    # Calculate diff in seconds, NaTs in the expresson result in NaTs, which is okay
    confirmations['diff_in_seconds'] = (confirmations['time_stamp'] - confirmations['lag'])/pd.Timedelta(seconds=1)
    
    # Fetch distinct user_ids whose diff in seconds is less than 1 day equivalent
    return confirmations[confirmations['diff_in_seconds']<=24*60*60][['user_id']].drop_duplicates()

