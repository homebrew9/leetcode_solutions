-- Oracle
/* Write your PL/SQL query statement below */
select f.follower, count(distinct f1.follower) as num
from follow f
     inner join follow f1 on (f1.followee = f.follower)
group by f.follower
order by follower
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select f.follower, count(distinct f1.follower) as num
from follow f
     inner join follow f1 on (f1.followee = f.follower)
group by f.follower
order by follower
;


-- SQL Server
/* Write your T-SQL query statement below */
select f.follower, count(distinct f1.follower) as num
from follow f
     inner join follow f1 on (f1.followee = f.follower)
group by f.follower
order by follower
;


# MySQL
# Write your MySQL query statement below
select f.follower, count(distinct f1.follower) as num
from follow f
     inner join follow f1 on (f1.followee = f.follower)
group by f.follower
order by follower
;


# Pandas
import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    return ( follow
            .merge(follow, how='inner', left_on='follower', right_on='followee')[['follower_x','follower_y']]
            .drop_duplicates()
            .groupby('follower_x', as_index=False)['follower_y']
            .count()
            .rename(columns={'follower_x':'follower', 'follower_y':'num'})
            .sort_values('follower')
           )

