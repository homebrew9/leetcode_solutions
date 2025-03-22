-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       DATEDIFF( DAY,
                 lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id),
                 purchase_date
               ) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       #purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
       DATEDIFF(purchase_date , lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id)) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


# Pandas
import pandas as pd

def find_valid_users(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases.sort_values(['user_id', 'purchase_date'], inplace=True)
    purchases['prev_user_id'] = purchases['user_id'].shift(1)
    purchases['prev_purchase_date'] = purchases['purchase_date'].shift(1)
    purchases['diff'] = ( np.where(
                              (~purchases['prev_user_id'].isna()) & (purchases['user_id']==purchases['prev_user_id']),
                              (purchases['purchase_date'] - purchases['prev_purchase_date']) / np.timedelta64(1,'D'),
                              np.NaN
                          )
                        )
    return purchases[purchases['diff'] <= 7][['user_id']].drop_duplicates().sort_values('user_id')

