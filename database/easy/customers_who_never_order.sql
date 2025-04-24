-- Oracle
/* Write your PL/SQL query statement below */
select c.name as customers
  from customers c
 where not exists (select null
                     from orders o
                    where o.customerId = c.id
                  )
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select c.name as "Customers"
  from customers c
 where c.id not in
 (
     select o.customerid
       from orders o
 )
;


# MySQL
# Write your MySQL query statement below
select c.name as customers
from customers c
where c.id not in (select o.customerid from orders o)
;


# Pandas
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers['id'].isin(orders.customerId)][['name']].rename(columns={'name': 'Customers'})

