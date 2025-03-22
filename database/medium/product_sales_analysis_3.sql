-- Oracle
/* Write your PL/SQL query statement below */
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


# MySQL
# Write your MySQL query statement below
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


# Pandas

