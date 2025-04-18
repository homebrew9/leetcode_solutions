-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return ( users
            .merge(rides, how='left', left_on='id', right_on='user_id')
            .groupby(['id_x','name'],as_index=0)['distance']
            .sum()
            .sort_values(by=['distance','name'], ascending=[False,True])[['name','distance']]
            .rename(columns={'distance': 'travelled_distance'})
           )

