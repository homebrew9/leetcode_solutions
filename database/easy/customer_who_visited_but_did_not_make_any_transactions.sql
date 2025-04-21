-- Oracle
/* Write your PL/SQL query statement below */
select v.customer_id as "customer_id", count(v.visit_id) as "count_no_trans"
from visits v
where not exists (select null from transactions t where t.visit_id = v.visit_id)
group by v.customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select v.customer_id,
       count(v.visit_id) as count_no_trans
  from visits v
 where not exists ( select null
                      from transactions t
                     where t.visit_id = v.visit_id
                  )
 group by v.customer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select v.customer_id,
       count(v.visit_id) as count_no_trans
  from visits v
 where not exists ( select null
                      from transactions t
                     where t.visit_id = v.visit_id
                  )
 group by v.customer_id
;


# MySQL
# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans
from visits v
where not exists (select null from transactions t where t.visit_id = v.visit_id)
group by v.customer_id
;


# Pandas
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return ( visits[~visits['visit_id'].isin(transactions['visit_id'])]
            .groupby('customer_id', as_index=0)
            .agg(count_no_trans=('visit_id', 'count'))
           )

