-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select c.salesperson_id, sum(s.price) as total
      from customer c
           inner join sales s on (s.customer_id = c.customer_id)
     group by c.salesperson_id
)
select sp.salesperson_id, sp.name, coalesce(t.total, 0) as total
from salesperson sp
     left outer join t on (t.salesperson_id = sp.salesperson_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select c.salesperson_id, sum(s.price) as total
      from customer c
           inner join sales s on (s.customer_id = c.customer_id)
     group by c.salesperson_id
)
select sp.salesperson_id, sp.name, coalesce(t.total, 0) as total
from salesperson sp
     left outer join t on (t.salesperson_id = sp.salesperson_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select c.salesperson_id, sum(s.price) as total
      from customer c
           inner join sales s on (s.customer_id = c.customer_id)
     group by c.salesperson_id
)
select sp.salesperson_id, sp.name, coalesce(t.total, 0) as total
from salesperson sp
     left outer join t on (t.salesperson_id = sp.salesperson_id)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select c.salesperson_id, sum(s.price) as total
      from customer c
           inner join sales s on (s.customer_id = c.customer_id)
     group by c.salesperson_id
)
select sp.salesperson_id, sp.name, coalesce(t.total, 0) as total
from salesperson sp
     left outer join t on (t.salesperson_id = sp.salesperson_id)
;


# Pandas
import pandas as pd

def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = customer.merge(sales, how='inner', on='customer_id').groupby('salesperson_id',as_index=False)['price'].sum()
    return salesperson.merge(df, how='left', on='salesperson_id').fillna(0).rename(columns={'price':'total'})

