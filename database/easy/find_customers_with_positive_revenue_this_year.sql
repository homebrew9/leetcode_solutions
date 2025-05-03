-- Oracle
/* Write your PL/SQL query statement below */
select customer_id
  from customers
 where year = 2021
 group by customer_id
having sum(revenue) > 0
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select customer_id
from customers
where year = 2021
and revenue > 0
;


-- SQL Server
/* Write your T-SQL query statement below */
select customer_id
from customers
where year = 2021
and revenue > 0
;


# MySQL
# Write your MySQL query statement below
select customer_id
from customers
where year = 2021
and revenue > 0
;


# Pandas
import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    return customers[(customers['year'] == 2021) & (customers['revenue'] > 0)][['customer_id']]

