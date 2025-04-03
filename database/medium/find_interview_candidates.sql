-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, contest_id, medal) as (
select gold_medal, contest_id, 'gold' from contests union all
select silver_medal, contest_id, 'silver' from contests union all
select bronze_medal, contest_id, 'bronze' from contests
),
t1 (user_id) as (
select user_id
from t
where medal = 'gold'
group by user_id
having count(distinct contest_id) >= 3
),
t2 as (
select distinct x.user_id
from t x
     inner join t y on (y.user_id = x.user_id and y.contest_id = x.contest_id + 1)
     inner join t z on (z.user_id = y.user_id and z.contest_id = y.contest_id + 1)
)
select u.name, u.mail
from users u
where u.user_id in (
    select user_id from t1
    union
    select user_id from t2
)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, contest_id, medal) as (
select gold_medal, contest_id, 'gold' from contests union all
select silver_medal, contest_id, 'silver' from contests union all
select bronze_medal, contest_id, 'bronze' from contests
),
t1 (user_id) as (
select user_id
from t
where medal = 'gold'
group by user_id
having count(distinct contest_id) >= 3
),
t2 as (
select distinct x.user_id
from t x
     inner join t y on (y.user_id = x.user_id and y.contest_id = x.contest_id + 1)
     inner join t z on (z.user_id = y.user_id and z.contest_id = y.contest_id + 1)
)
select u.name, u.mail
from users u
where u.user_id in (
    select user_id from t1
    union
    select user_id from t2
)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, contest_id, medal) as (
select gold_medal, contest_id, 'gold' from contests union all
select silver_medal, contest_id, 'silver' from contests union all
select bronze_medal, contest_id, 'bronze' from contests
),
t1 (user_id) as (
select user_id
from t
where medal = 'gold'
group by user_id
having count(distinct contest_id) >= 3
),
t2 as (
select distinct x.user_id
from t x
     inner join t y on (y.user_id = x.user_id and y.contest_id = x.contest_id + 1)
     inner join t z on (z.user_id = y.user_id and z.contest_id = y.contest_id + 1)
)
select u.name, u.mail
from users u
where u.user_id in (
    select user_id from t1
    union
    select user_id from t2
)
;


# MySQL
# Write your MySQL query statement below
with t (user_id, contest_id, medal) as (
select gold_medal, contest_id, 'gold' from contests union all
select silver_medal, contest_id, 'silver' from contests union all
select bronze_medal, contest_id, 'bronze' from contests
),
t1 (user_id) as (
select user_id
from t
where medal = 'gold'
group by user_id
having count(distinct contest_id) >= 3
),
t2 as (
select distinct x.user_id
from t x
     inner join t y on (y.user_id = x.user_id and y.contest_id = x.contest_id + 1)
     inner join t z on (z.user_id = y.user_id and z.contest_id = y.contest_id + 1)
)
select u.name, u.mail
from users u
where u.user_id in (
    select user_id from t1
    union
    select user_id from t2
)
;


# Pandas
import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    df = ( contests
          .melt(id_vars='contest_id',
                value_vars=['gold_medal','silver_medal','bronze_medal'],
                var_name='medal', value_name='user_id'
               )
         )
    triple_gold_medalist = ( df[df['medal'] == 'gold_medal']
                            .groupby('user_id', as_index=0)['contest_id']
                            .count()
                            .query('contest_id >= 3')['user_id']
                           )
    df = df.sort_values(['user_id','contest_id']).reset_index(drop=True)
    df['rn'] = df.groupby('user_id', as_index=0).cumcount()
    df['group_id'] = df['contest_id'] - df['rn']
    triple_consecutive_medalist = ( df
                                   .groupby(['user_id','group_id'], as_index=0)['contest_id']
                                   .count()
                                   .query('contest_id >= 3')['user_id']
                                  )
    return ( df[df['user_id'].isin(triple_gold_medalist) | df['user_id'].isin(triple_consecutive_medalist)][['user_id']]
            .drop_duplicates()
            .merge(users, how='inner', on='user_id')[['name','mail']]
           )

