-- Oracle


-- PostgreSQL


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

