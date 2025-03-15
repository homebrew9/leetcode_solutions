-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select trx.customer_id, prd.category, trx.transaction_id, trx.transaction_date,
           count(*) over (partition by trx.customer_id, prd.category) as most_frequent_category
      from transactions trx
           inner join products prd on (prd.product_id = trx.product_id)
),
t1 as (
    select customer_id, category, transaction_id, transaction_date, most_frequent_category,
           dense_rank() over (partition by customer_id
                              order by most_frequent_category desc, transaction_date desc
                             ) as drnk
      from t
),
t2 as (
    select customer_id, category
      from t1
     where drnk = 1
)
select t.customer_id,
       round(sum(t.amount), 2) as total_amount,
       count(t.transaction_id) as transaction_count,
       count(distinct p.category) as unique_categories,
       round(avg(t.amount), 2) as avg_transaction_amount,
       t2.category as top_category,
       round((count(t.transaction_id) * 10) + (sum(t.amount) / 100), 2) as loyalty_score
  from transactions t
       inner join products p on (p.product_id = t.product_id)
       inner join t2 on (t2.customer_id = t.customer_id)
 group by t.customer_id, t2.category
 order by loyalty_score desc, customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select trx.customer_id, prd.category, trx.transaction_id, trx.transaction_date,
           count(*) over (partition by trx.customer_id, prd.category) as most_frequent_category
      from transactions trx
           inner join products prd on (prd.product_id = trx.product_id)
),
t1 as (
    select customer_id, category, transaction_id, transaction_date, most_frequent_category,
           dense_rank() over (partition by customer_id
                              order by most_frequent_category desc, transaction_date desc
                             ) as drnk
      from t
),
t2 as (
    select customer_id, category
      from t1
     where drnk = 1
)
select t.customer_id,
       round(sum(t.amount), 2) as total_amount,
       count(t.transaction_id) as transaction_count,
       count(distinct p.category) as unique_categories,
       round(avg(t.amount), 2) as avg_transaction_amount,
       t2.category as top_category,
       round((count(t.transaction_id) * 10) + (sum(t.amount) / 100), 2) as loyalty_score
  from transactions t
       inner join products p on (p.product_id = t.product_id)
       inner join t2 on (t2.customer_id = t.customer_id)
 group by t.customer_id, t2.category
 order by loyalty_score desc, customer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select trx.customer_id, prd.category, trx.transaction_id, trx.transaction_date,
           count(*) over (partition by trx.customer_id, prd.category) as most_frequent_category
      from transactions trx
           inner join products prd on (prd.product_id = trx.product_id)
),
t1 as (
    select customer_id, category, transaction_id, transaction_date, most_frequent_category,
           dense_rank() over (partition by customer_id
                              order by most_frequent_category desc, transaction_date desc
                             ) as drnk
      from t
),
t2 as (
    select customer_id, category
      from t1
     where drnk = 1
)
select t.customer_id,
       round(sum(t.amount), 2) as total_amount,
       count(t.transaction_id) as transaction_count,
       count(distinct p.category) as unique_categories,
       round(avg(t.amount), 2) as avg_transaction_amount,
       t2.category as top_category,
       round((count(t.transaction_id) * 10) + (sum(t.amount) / 100), 2) as loyalty_score
  from transactions t
       inner join products p on (p.product_id = t.product_id)
       inner join t2 on (t2.customer_id = t.customer_id)
 group by t.customer_id, t2.category
 order by loyalty_score desc, customer_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select trx.customer_id, prd.category, trx.transaction_id, trx.transaction_date,
           count(*) over (partition by trx.customer_id, prd.category) as most_frequent_category
      from transactions trx
           inner join products prd on (prd.product_id = trx.product_id)
),
t1 as (
    select customer_id, category, transaction_id, transaction_date, most_frequent_category,
           dense_rank() over (partition by customer_id
                              order by most_frequent_category desc, transaction_date desc
                             ) as drnk
      from t
),
t2 as (
    select customer_id, category
      from t1
     where drnk = 1
)
select t.customer_id,
       round(sum(t.amount), 2) as total_amount,
       count(t.transaction_id) as transaction_count,
       count(distinct p.category) as unique_categories,
       round(avg(t.amount), 2) as avg_transaction_amount,
       t2.category as top_category,
       round((count(t.transaction_id) * 10) + (sum(t.amount) / 100), 2) as loyalty_score
  from transactions t
       inner join products p on (p.product_id = t.product_id)
       inner join t2 on (t2.customer_id = t.customer_id)
 group by t.customer_id, t2.category
 order by loyalty_score desc, customer_id
;


# Pandas
import pandas as pd

def analyze_customer_behavior(transactions: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = ( transactions
          .merge(products, how='inner', on='product_id')
          .groupby('customer_id', as_index=0)
          .agg(total_amount = ('amount', 'sum'),
               transaction_count=('transaction_id', 'count'),
               unique_categories=('category', 'nunique'),
               avg_transaction_amount = ('amount', 'mean')
              )
         )
    df1 = ( transactions
           .merge(products, how='inner', on='product_id')
           .groupby(['customer_id','category'], as_index=0)
           .agg(category_count=('transaction_id', 'count'))
          )
    df2 = ( transactions
           .merge(products, how='inner', on='product_id')
           .merge(df1, how='inner', on=['customer_id', 'category'])
           .sort_values(['customer_id','category_count','transaction_date'], ascending=[1,0,0])
          )
    df2 = ( df2
           .assign(drnk=df2.groupby(['customer_id'], as_index=0).cumcount()+1)
           .query('drnk == 1')[['customer_id','category']]
           .rename(columns={'category': 'top_category'})
          )
    df = df.merge(df2, how='inner', on='customer_id')
    df['loyalty_score'] = df['transaction_count'] * 10 + df['total_amount'] / 100
    # Workaround for rounding bug!
    my_rounding = lambda x: round(x+.00001, 2)
    df['total_amount'] = df['total_amount'].apply(my_rounding)
    df['avg_transaction_amount'] = df['avg_transaction_amount'].apply(my_rounding)
    df['loyalty_score'] = df['loyalty_score'].apply(my_rounding)
    df.sort_values(by=['loyalty_score', 'customer_id'], ascending=[0,0], inplace=True)
    return df

