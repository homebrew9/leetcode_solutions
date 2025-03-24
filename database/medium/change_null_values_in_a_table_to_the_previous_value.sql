-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select row_number() over (order by null) as rn, id, drink
      from coffeeshop
)
select id,
       coalesce(drink, lag(drink ignore nulls) over (order by rn)) as drink
  from t
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

