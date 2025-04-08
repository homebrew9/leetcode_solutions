-- Oracle
/* Write your PL/SQL query statement below */
select count(sub.account_id) as accounts_count
from subscriptions sub
where DATE'2021-01-01' between trunc(sub.start_date) and trunc(sub.end_date)
and not exists (
    select null
    from streams str
    where str.account_id = sub.account_id
    and trunc(stream_date, 'YYYY') = DATE'2021-01-01'
)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select count(sub.account_id) as accounts_count
from subscriptions sub
where '2021-01-01' between sub.start_date and sub.end_date
and not exists (
    select null
    from streams str
    where str.account_id = sub.account_id
    and date_part('year', stream_date) = 2021
)
;


-- SQL Server
/* Write your T-SQL query statement below */
select count(sub.account_id) as accounts_count
from subscriptions sub
where '2021-01-01' between sub.start_date and sub.end_date
and not exists (
    select null
    from streams str
    where str.account_id = sub.account_id
    and YEAR(stream_date) = 2021
)
;


# MySQL
# Write your MySQL query statement below
select count(sub.account_id) as accounts_count
from subscriptions sub
where '2021-01-01' between sub.start_date and sub.end_date
and not exists (
    select null
    from streams str
    where str.account_id = sub.account_id
    and YEAR(stream_date) = 2021
)
;


# Pandas
import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    streamed_in_2021 = streams.query('stream_date.dt.strftime("%Y") == "2021"')
    accounts_count = ( subscriptions
                      .query('start_date <= "2021-01-01" and "2021-01-01" <= end_date')
                      .merge(streamed_in_2021, how='left', on='account_id')
                      .query('session_id.isnull()')['account_id']
                      .count()
                     )
    return pd.DataFrame(data={'accounts_count': [accounts_count]})

