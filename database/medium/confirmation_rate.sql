-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, total_requested) as (
    select user_id, count(*) as total_requested
      from confirmations
     group by user_id
),
t1 (user_id, total_confirmed) as (
    select user_id, count(*) as total_confirmed
      from confirmations
     where action = 'confirmed'
     group by user_id
)
select t1.user_id, round(t1.total_confirmed/t.total_requested, 2) as confirmation_rate
from t
     inner join t1 on (t1.user_id = t.user_id)
union all
select s.user_id, 0.00 as confirmation_rate
  from signups s
 where not exists (select null from t1 where t1.user_id = s.user_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select s.user_id,
       round(sum(case when c.action = 'confirmed' then 1 else 0 end) / count(*)::numeric, 2) as confirmation_rate
  from signups s
       inner join confirmations c on (c.user_id = s.user_id)
 group by s.user_id
union all
select distinct s1.user_id, 0 as confirmation_rate
  from signups s1
 where not exists (select null from confirmations c1 where c1.user_id = s1.user_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select s.user_id,
       round(sum(case when c.action = 'confirmed' then 1 else 0 end) / convert(float, count(*)), 2) as confirmation_rate
  from signups s
       inner join confirmations c on (c.user_id = s.user_id)
 group by s.user_id
union all
select distinct s1.user_id, 0 as confirmation_rate
  from signups s1
 where not exists (select null from confirmations c1 where c1.user_id = s1.user_id)
;


# MySQL
# Write your MySQL query statement below
select s.user_id,
       round(sum(case when c.action = 'confirmed' then 1 else 0 end) / count(*), 2) as confirmation_rate
  from signups s
       inner join confirmations c on (c.user_id = s.user_id)
 group by s.user_id
union all
select distinct s1.user_id, 0 as confirmation_rate
  from signups s1
 where not exists (select null from confirmations c1 where c1.user_id = s1.user_id)
;


# Pandas
import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    confirmations['confirmed_action'] = np.where(confirmations['action']=='confirmed', 1, 0)
    df = signups.merge(confirmations, how='inner', on='user_id').groupby('user_id', as_index=0).agg({'confirmed_action': 'sum', 'action': 'count'})
    df['confirmation_rate'] = round(df['confirmed_action'] / df['action'], 2)
    df = df[['user_id', 'confirmation_rate']]
    df1 = signups[~signups['user_id'].isin(confirmations['user_id'])][['user_id']]
    df1['confirmation_rate'] = 0
    return pd.concat([df, df1])

