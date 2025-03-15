-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select a.id, a.login_date,
       row_number() over (partition by a.id order by a.login_date) as rn,
       a.login_date - row_number() over (partition by a.id order by a.login_date)::int as group_id
from (
        select distinct id, login_date
        from logins
     ) a
)
select distinct a.id, a.name
from accounts a
     inner join t on (t.id = a.id)
group by a.id, a.name, t.group_id
having max(t.login_date) - min(t.login_date) + 1 >= 5
order by a.id
;


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    '''
            ----+----------+-------
            col |  rownum  | diff
            ----+----------+-------
             1  |     0    |   1
             2  |     1    |   1
             5  |     2    |   3
             6  |     3    |   3
             7  |     4    |   3
            10  |     5    |   5
            13  |     6    |   7
            ----+----------+-------
        Notice that if a column value repeats then its difference with a running number stays the same.
        We will exploit this fact in the code below. Our "col" value is the difference (in days) of
        login_date from an epoch. Once we have the "diff" column, a simple "groupby" does the rest.
    '''
    df = logins.drop_duplicates()
    df = df.merge(accounts, on='id').sort_values(['id','login_date'])
    df['row_nb'] = range(len(df))
    df['date_idx'] = (df['login_date'] - pd.Timestamp('2020-01-01')).dt.days
    df['diff_group'] = df['date_idx'] - df['row_nb']
    df = df.groupby(['id','name','diff_group'], as_index=0)['row_nb'].count()
    return df.query('row_nb >= 5')[['id','name']].drop_duplicates()

