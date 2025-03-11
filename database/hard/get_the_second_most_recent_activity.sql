-- Oracle
/* Write your PL/SQL query statement below */
with t (username, activity, startdate, enddate, drnk, cnt) as (
select username, activity, startdate, enddate,
       dense_rank() over (partition by username order by startdate desc) as drnk,
       count(*) over (partition by username) as cnt
from useractivity
)
select username, activity,
       to_char(startdate, 'YYYY-MM-DD') as startdate,
       to_char(enddate, 'YYYY-MM-DD') as enddate
from t
where (cnt = 1 or (cnt > 1 and drnk = 2))
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (username, activity, startdate, enddate, drnk, cnt) as (
select username, activity, startdate, enddate,
       dense_rank() over (partition by username order by startdate desc) as drnk,
       count(*) over (partition by username) as cnt
from useractivity
)
select username, activity, startdate, enddate
from t
where (cnt = 1 or (cnt > 1 and drnk = 2))
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (username, activity, startdate, enddate, drnk, cnt) as (
select username, activity, startdate, enddate,
       dense_rank() over (partition by username order by startdate desc) as drnk,
       count(*) over (partition by username) as cnt
from useractivity
)
select username, activity, startdate, enddate
from t
where (cnt = 1 or (cnt > 1 and drnk = 2))
;


# MySQL
# Write your MySQL query statement below
with t (username, activity, startdate, enddate, drnk, cnt) as (
select username, activity, startdate, enddate,
       dense_rank() over (partition by username order by startdate desc) as drnk,
       count(*) over (partition by username) as cnt
from useractivity
)
select username, activity, startdate, enddate
from t
where (cnt = 1 or (cnt > 1 and drnk = 2))
;


# Pandas
import pandas as pd

def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:
    user_activity = user_activity.assign(
                        drnk=user_activity.groupby('username')['startDate'].rank(method='dense',ascending=False),
                        cnt=user_activity.groupby('username')['startDate'].transform('count')
                    )
    return user_activity[(user_activity['cnt']==1) | (user_activity['drnk']==2)][['username','activity','startDate','endDate']]

