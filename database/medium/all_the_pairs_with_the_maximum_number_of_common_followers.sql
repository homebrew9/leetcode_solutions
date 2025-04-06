-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t (user1_id, user2_id, follower_count) as (
select x.user_id, y.user_id, count(*) as followers_count
from relations x
     inner join relations y on (x.user_id < y.user_id and x.follower_id = y.follower_id)
group by x.user_id, y.user_id
)
select user1_id, user2_id
from t
where follower_count = (select max(follower_count) from t)
;


# MySQL
# Write your MySQL query statement below
with t (user1_id, user2_id, follower_count) as (
select x.user_id, y.user_id, count(*) as followers_count
from relations x
     inner join relations y on (x.user_id < y.user_id and x.follower_id = y.follower_id)
group by x.user_id, y.user_id
#order by x.user_id, y.user_id
)
select user1_id, user2_id
from t
where follower_count = (select max(follower_count) from t)
;


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

