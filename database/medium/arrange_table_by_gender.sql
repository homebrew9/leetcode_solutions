-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    genders['rnk'] = ( genders
                      .sort_values(['gender','user_id'])
                      .groupby('gender', as_index=0)
                      .cumcount()+1
                     )
    genders['order'] = np.where(genders['gender'] == 'female', 1, np.where(genders['gender'] == 'other', 2, 3))
    return genders.sort_values(['rnk','order'])[['user_id', 'gender']]

