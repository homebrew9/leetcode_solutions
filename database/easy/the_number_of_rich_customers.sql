-- Oracle
/* Write your PL/SQL query statement below */
select count(distinct customer_id) as "rich_count"
from store
where amount > 500
;


-- PostgreSQL
-- The option for PostgreSQL is not available in the drop-down.

-- SQL Server
/* Write your T-SQL query statement below */
select count(distinct customer_id) as "rich_count"
from store
where amount > 500
;


# MySQL
# Write your MySQL query statement below
select count(distinct customer_id) as rich_count
  from store
 where amount > 500
;


# Pandas
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_count = store[store['amount'] > 500]['customer_id'].nunique()
    return pd.DataFrame(data={'rich_count': [rich_count]})
    
