-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


# MySQL
# Write your MySQL query statement below
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


# Pandas
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    return ( logs
            .merge(logs, how='inner', on='num')
            .query('id_y == id_x + 1')
            .merge(logs, how='inner', on='num')
            .query('id == id_y + 1')[['num']]
            .drop_duplicates()
            .rename(columns={'num': 'ConsecutiveNums'})
           )

# Pandas Version 1
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['prev_num'] = logs[['num']].shift(1)
    logs['prev_to_prev_num'] = logs[['num']].shift(2)
    return ( logs[(logs['num']==logs['prev_num']) & (logs['num']==logs['prev_to_prev_num'])][['num']]
            .drop_duplicates()
            .rename(columns={'num': 'ConsecutiveNums'})
           )

