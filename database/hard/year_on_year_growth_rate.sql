-- Oracle
/* Write your PL/SQL query statement below */
with t (year, product_id, curr_year_spend) as (
    select to_number(to_char(transaction_date, 'yyyy')), product_id, sum(spend)
      from user_transactions
     group by to_char(transaction_date, 'yyyy'), product_id
),
t1 as (
    select year, product_id, curr_year_spend,
           lag(curr_year_spend) over (partition by product_id order by year) as prev_year_spend
      from t
)
select year, product_id, curr_year_spend, prev_year_spend,
       round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate
  from t1
 order by product_id, year
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (year, product_id, curr_year_spend) as (
    select to_char(transaction_date, 'yyyy')::int, product_id, sum(spend)
      from user_transactions
     group by to_char(transaction_date, 'yyyy'), product_id
),
t1 as (
    select year, product_id, curr_year_spend,
           lag(curr_year_spend) over (partition by product_id order by year) as prev_year_spend
      from t
)
select year, product_id, curr_year_spend, prev_year_spend,
       round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate
  from t1
 order by product_id, year
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (year, product_id, curr_year_spend) as (
    select year(transaction_date), product_id, sum(spend)
      from user_transactions
     group by year(transaction_date), product_id
),
t1 as (
    select year, product_id, curr_year_spend,
           lag(curr_year_spend) over (partition by product_id order by year) as prev_year_spend
      from t
)
select year, product_id, curr_year_spend, prev_year_spend,
       round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate
  from t1
 order by product_id, year
;


# MySQL
# Write your MySQL query statement below
with t (year, product_id, curr_year_spend) as (
    select year(transaction_date), product_id, sum(spend)
      from user_transactions
     group by year(transaction_date), product_id
),
t1 as (
    select year, product_id, curr_year_spend,
           lag(curr_year_spend) over (partition by product_id order by year) as prev_year_spend
      from t
)
select year, product_id, curr_year_spend, prev_year_spend,
       round((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) as yoy_rate
  from t1
 order by product_id, year
;


# Pandas
import pandas as pd

def calculate_yoy_growth(user_transactions: pd.DataFrame) -> pd.DataFrame:
    user_transactions['transaction_date'] = pd.to_datetime(user_transactions['transaction_date'])
    user_transactions['year'] = user_transactions['transaction_date'].dt.year
    df = ( user_transactions
          .groupby(['year', 'product_id'], as_index=0)['spend']
          .sum()
          .sort_values(['product_id','year'])
         )
    df['prev_year_spend'] = df.shift(1)['spend']
    df['prev_product_id'] = df.shift(1)['product_id']
    df['prev_year_spend'] = np.where(df['product_id'] != df['prev_product_id'], np.nan, df['prev_year_spend'])
    df['yoy_rate'] = round((df['spend'] - df['prev_year_spend'])/df['prev_year_spend'] * 100, 2)
    df.rename(columns={'spend': 'curr_year_spend'}, inplace=1)
    return df[['year', 'product_id', 'curr_year_spend', 'prev_year_spend', 'yoy_rate']]

