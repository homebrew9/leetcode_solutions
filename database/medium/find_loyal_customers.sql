-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_id, transaction_date, transaction_type, n_purchases, n_days, n_refund_rate) as (
    select customer_id, transaction_date, transaction_type,
           sum(case when transaction_type = 'purchase' then 1 else 0 end) over (partition by customer_id) as n_purchases,
           max(transaction_date) over (partition by customer_id)
           -
           min(transaction_date) over (partition by customer_id) as n_days,
           sum(case when transaction_type = 'refund' then 1 else 0 end) over (partition by customer_id)
           /
           count(*) over (partition by customer_id) as n_refund_rate
      from customer_transactions
)
select distinct customer_id
  from t
 where n_purchases >= 3
   and n_days >= 30
   and n_refund_rate < 0.2
 order by customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (customer_id, transaction_date, transaction_type, n_purchases, n_days, n_refund_rate) as (
    select customer_id, transaction_date, transaction_type,
           sum(case when transaction_type = 'purchase' then 1 else 0 end) over (partition by customer_id) as n_purchases,
           max(transaction_date) over (partition by customer_id)
           -
           min(transaction_date) over (partition by customer_id) as n_days,
           sum(case when transaction_type = 'refund' then 1 else 0 end) over (partition by customer_id)
           /
           (count(*) over (partition by customer_id))::numeric as n_refund_rate
      from customer_transactions
)
select distinct customer_id
  from t
 where n_purchases >= 3
   and n_days >= 30
   and n_refund_rate < 0.2
 order by customer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, transaction_date, transaction_type, n_purchases, n_days, n_refund_rate) as (
    select customer_id, transaction_date, transaction_type,
           sum(case when transaction_type = 'purchase' then 1 else 0 end) over (partition by customer_id) as n_purchases,
           DATEDIFF(
               DAY,
               min(transaction_date) over (partition by customer_id),
               max(transaction_date) over (partition by customer_id)
           ) as n_days,
           sum(case when transaction_type = 'refund' then 1 else 0 end) over (partition by customer_id)
           /
           CONVERT(NUMERIC, count(*) over (partition by customer_id)) as n_refund_rate
      from customer_transactions
)
select distinct customer_id
  from t
 where n_purchases >= 3
   and n_days >= 30
   and n_refund_rate < 0.2
 order by customer_id
;


# MySQL
# Write your MySQL query statement below
with t (customer_id, transaction_date, transaction_type, n_purchases, n_days, n_refund_rate) as (
    select customer_id, transaction_date, transaction_type,
           sum(case when transaction_type = 'purchase' then 1 else 0 end) over (partition by customer_id) as n_purchases,
           TIMESTAMPDIFF(
               DAY,
               min(transaction_date) over (partition by customer_id),
               max(transaction_date) over (partition by customer_id)
           ) as n_days,
           sum(case when transaction_type = 'refund' then 1 else 0 end) over (partition by customer_id)
           /
           count(*) over (partition by customer_id) as n_refund_rate
      from customer_transactions
)
select distinct customer_id
  from t
 where n_purchases >= 3
   and n_days >= 30
   and n_refund_rate < 0.2
 order by customer_id
;


# Pandas
import pandas as pd
import numpy as np

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    min_purchase_customers = ( customer_transactions
                              .query('transaction_type == "purchase"')
                              .groupby('customer_id', as_index=0)
                              .size()
                              .query('size >= 3')['customer_id']
                             )
    customer_transactions['transaction_date'] = pd.to_datetime(customer_transactions['transaction_date'])
    df_activity = ( customer_transactions
                   .groupby('customer_id', as_index=0)
                   .agg(min_date=('transaction_date', 'min'), max_date=('transaction_date', 'max'))
                  )
    df_activity['diff'] = (df_activity['max_date'] - df_activity['min_date']).dt.days
    min_activity_customers = df_activity.query('diff >= 30')['customer_id']
    customer_transactions['is_refund'] = np.where(customer_transactions['transaction_type']=='refund',1,0)
    df_refund = ( customer_transactions
                 .groupby('customer_id', as_index=0)
                 .agg(refund_trx=('is_refund', 'sum'), total_trx=('transaction_id', 'count'))
                )
    df_refund['refund_rate'] = df_refund['refund_trx'] / df_refund['total_trx']
    refund_rate_customers = df_refund.query('refund_rate < 0.2')['customer_id']
    return ( customer_transactions[
               (customer_transactions['customer_id'].isin(min_purchase_customers)) &
               (customer_transactions['customer_id'].isin(min_activity_customers)) &
               (customer_transactions['customer_id'].isin(refund_rate_customers))
             ][['customer_id']]
            .drop_duplicates()
            .sort_values('customer_id')
           )







