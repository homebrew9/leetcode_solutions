-- Oracle
/* Write your PL/SQL query statement below */
with t (transaction_id, customer_id, transaction_date, amount, first_trx_date, lvl) as (
    select transaction_id, customer_id, transaction_date, amount, transaction_date, 1 as lvl
      from transactions
    union all
    select x.transaction_id, x.customer_id, x.transaction_date, x.amount, t.first_trx_date, t.lvl + 1
      from transactions x
           inner join t on ( x.customer_id = t.customer_id and
                             x.transaction_date = t.transaction_date + 1 and
                             x.amount > t.amount
                           )
),
t1 (customer_id, consecutive_start, consecutive_end) as (
select customer_id,
       min(transaction_date) as consecutive_start,
       max(transaction_date) as consecutive_end
from t
where (customer_id, first_trx_date) in (select customer_id, first_trx_date from t where lvl >= 3)
group by customer_id, first_trx_date
)
select customer_id,
       to_char(min(consecutive_start), 'YYYY-MM-DD') as consecutive_start,
       to_char(consecutive_end, 'YYYY-MM-DD') as consecutive_end
from t1
group by customer_id, consecutive_end
order by customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (transaction_id, customer_id, transaction_date, amount, first_trx_date, lvl) as (
    select transaction_id, customer_id, transaction_date, amount, transaction_date, 1 as lvl
      from transactions
    union all
    select x.transaction_id, x.customer_id, x.transaction_date, x.amount, t.first_trx_date, t.lvl + 1
      from transactions x
           inner join t on ( x.customer_id = t.customer_id and
                             x.transaction_date = t.transaction_date + 1 and
                             x.amount > t.amount
                           )
),
t1 (customer_id, consecutive_start, consecutive_end) as (
select customer_id,
       min(transaction_date) as consecutive_start,
       max(transaction_date) as consecutive_end
from t
where (customer_id, first_trx_date) in (select customer_id, first_trx_date from t where lvl >= 3)
group by customer_id, first_trx_date
)
select customer_id,
       min(consecutive_start) as consecutive_start,
       consecutive_end
from t1
group by customer_id, consecutive_end
order by customer_id, consecutive_start
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (transaction_id, customer_id, transaction_date, amount, first_trx_date, lvl) as (
    select transaction_id, customer_id, transaction_date, amount, transaction_date, 1 as lvl
      from transactions
    union all
    select x.transaction_id, x.customer_id, x.transaction_date, x.amount, t.first_trx_date, t.lvl + 1
      from transactions x
           inner join t on ( x.customer_id = t.customer_id and
                             x.transaction_date = DATEADD(DAY, 1, t.transaction_date) and
                             x.amount > t.amount
                           )
),
t1 (customer_id, consecutive_start, consecutive_end) as (
select customer_id,
       min(transaction_date) as consecutive_start,
       max(transaction_date) as consecutive_end
from t
where exists (
    select null
      from t x
     where x.customer_id = t.customer_id
       and x.first_trx_date = t.first_trx_date
       and x.lvl >= 3
)
group by customer_id, first_trx_date
)
select customer_id,
       min(consecutive_start) as consecutive_start,
       consecutive_end
from t1
group by customer_id, consecutive_end
order by customer_id, consecutive_start
;


# MySQL
# Write your MySQL query statement below
with recursive t (transaction_id, customer_id, transaction_date, amount, first_trx_date, lvl) as (
    select transaction_id, customer_id, transaction_date, amount, transaction_date, 1 as lvl
      from transactions
    union all
    select x.transaction_id, x.customer_id, x.transaction_date, x.amount, t.first_trx_date, t.lvl + 1
      from transactions x
           inner join t on ( x.customer_id = t.customer_id and
                             x.transaction_date = DATE_ADD(t.transaction_date, INTERVAL 1 DAY) and
                             x.amount > t.amount
                           )
),
t1 (customer_id, consecutive_start, consecutive_end) as (
select customer_id,
       min(transaction_date) as consecutive_start,
       max(transaction_date) as consecutive_end
from t
#where (customer_id, first_trx_date) in (select customer_id, first_trx_date from t where lvl >= 3)
where exists (
    select null
      from t x
     where x.customer_id = t.customer_id
       and x.first_trx_date = t.first_trx_date
       and x.lvl >= 3
)
group by customer_id, first_trx_date
)
select customer_id,
       min(consecutive_start) as consecutive_start,
       consecutive_end
from t1
group by customer_id, consecutive_end
order by customer_id, consecutive_start
;

