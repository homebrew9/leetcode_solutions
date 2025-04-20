-- Oracle
/* Write your PL/SQL query statement below */
select r.contest_id, round(count(*)/u.user_count * 100, 2) as percentage
from register r
     cross join (select count(*) as user_count from users) u
group by r.contest_id, u.user_count
order by percentage desc, r.contest_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select r.contest_id, round(count(*) / u.total_users::numeric * 100, 2) as percentage
  from register r
       cross join (select count(*) as total_users from users) u
 group by r.contest_id, u.total_users
 order by percentage desc, r.contest_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select r.contest_id, round(count(*) / convert(float, u.total_users) * 100, 2) as percentage
  from register r
       cross join (select count(*) as total_users from users) u
 group by r.contest_id, u.total_users
 order by percentage desc, r.contest_id
;


# MySQL
# Write your MySQL query statement below
select r.contest_id, round(count(*) / u.total_users * 100, 2) as percentage
  from register r
       cross join (select count(*) as total_users from users) u
 group by r.contest_id, u.total_users
 order by percentage desc, r.contest_id
;


# Pandas
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby('contest_id', as_index=0).size().rename(columns={'size': 'percentage'})
    df['percentage'] = round(df['percentage'] / users.shape[0] * 100, 2)
    return df.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

