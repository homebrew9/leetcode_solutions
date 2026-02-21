-- Oracle # 1
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

-- Oracle # 2
-- Islands and gaps technique
with t as (
    select transaction_id, customer_id, transaction_date, amount,
        case when transaction_date = lag(transaction_date) over (partition by customer_id order by transaction_date) + 1
                    and amount > lag(amount) over (partition by customer_id order by transaction_date)
                then 0
                else 1
        end as marker
    from transactions
),
t1 as (
    select customer_id, transaction_date, marker,
        sum(marker) over (partition by customer_id order by transaction_date) as group_id
    from t
)
select customer_id,
       TO_CHAR(min(transaction_date), 'YYYY-MM-DD') as consecutive_start,
       TO_CHAR(max(transaction_date), 'YYYY-MM-DD') as consecutive_end
  from t1
 group by customer_id, group_id
having count(*) >= 3
 order by customer_id, consecutive_start, consecutive_end
;

-- Oracle # 3
-- The MATCH_RECOGNIZE clause works only on Oracle 12c and higher.
-- The LC Judge has Oracle 11.2, so it fails here.
SELECT customer_id, consecutive_start, consecutive_end
  FROM transactions
       MATCH_RECOGNIZE (
           PARTITION BY customer_id
           ORDER BY transaction_date
           MEASURES STRT.transaction_date         AS consecutive_start,
                    LAST(UP.transaction_date)     AS consecutive_end,
                    FINAL COUNT(transaction_date) AS up_days
           ONE ROW PER MATCH
           AFTER MATCH SKIP TO LAST UP
           PATTERN (STRT UP+)
           DEFINE
               UP AS UP.amount > PREV(UP.amount) AND UP.transaction_date = PREV(UP.transaction_date) + 1
       ) mr
 WHERE up_days >= 3
 ORDER BY customer_id, consecutive_start, consecutive_end
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


# Pandas

import pandas as pd

def consecutive_increasing_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(by=['customer_id','transaction_date'], ascending=[True,True], inplace=True)
    transactions['marker'] = np.where(
                                 (transactions['customer_id'] == transactions.shift(1)['customer_id']) &
                                 (transactions['transaction_date'] == transactions.shift(1)['transaction_date']
                                                                      + pd.Timedelta(days=1)) &
                                 (transactions['amount'] > transactions.shift(1)['amount']),
                                 0, 1
                             )
    return ( transactions
            .assign(group_id=transactions.groupby('customer_id')['marker'].cumsum())
            .groupby(['customer_id','group_id'], as_index=0)
            .agg(size=('transaction_id','count'),
                 consecutive_start=('transaction_date','min'),
                 consecutive_end=('transaction_date','max')
            )
            .query('size >= 3')[['customer_id','consecutive_start','consecutive_end']]
            .sort_values(['customer_id','consecutive_start','consecutive_end'])
           )


























