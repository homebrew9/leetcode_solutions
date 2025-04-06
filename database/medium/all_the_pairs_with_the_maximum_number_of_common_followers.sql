-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def find_pairs(relations: pd.DataFrame) -> pd.DataFrame:
    df = ( relations
          .merge(relations, how='inner', on='follower_id')
          .query('user_id_x < user_id_y')
          .groupby(['user_id_x','user_id_y'], as_index=False)['follower_id']
          .count()
         )
    return ( df[df['follower_id'] == df['follower_id'].max()][['user_id_x','user_id_y']]
            .rename(columns={'user_id_x':'user1_id', 'user_id_y':'user2_id'})
           )

