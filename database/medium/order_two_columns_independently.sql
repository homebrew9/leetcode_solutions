-- Oracle
/* Write your PL/SQL query statement below */
with t (rn, first_col) as (
select row_number() over (order by first_col) as rn, first_col
from data
),
u (rn, second_col) as (
select row_number() over (order by second_col desc) as rn, second_col
from data
)
select t.first_col, u.second_col
from t
     inner join u on (u.rn = t.rn)
order by t.rn
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (rn, first_col) as (
select row_number() over (order by first_col) as rn, first_col
from data
),
u (rn, second_col) as (
select row_number() over (order by second_col desc) as rn, second_col
from data
)
select t.first_col, u.second_col
from t
     inner join u on (u.rn = t.rn)
order by t.rn
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (rn, first_col) as (
select row_number() over (order by first_col) as rn, first_col
from data
),
u (rn, second_col) as (
select row_number() over (order by second_col desc) as rn, second_col
from data
)
select t.first_col, u.second_col
from t
     inner join u on (u.rn = t.rn)
order by t.rn
;


# MySQL
# Write your MySQL query statement below
with t (rn, first_col) as (
select row_number() over (order by first_col) as rn, first_col
from data
),
u (rn, second_col) as (
select row_number() over (order by second_col desc) as rn, second_col
from data
)
select t.first_col, u.second_col
from t
     inner join u on (u.rn = t.rn)
order by t.rn
;


# Pandas
import pandas as pd

def order_two_columns(data: pd.DataFrame) -> pd.DataFrame:
    fc = data['first_col'].sort_values().reset_index(drop=True)
    sc = data['second_col'].sort_values(ascending=False).reset_index(drop=True)
    return pd.DataFrame({'first_col': fc, 'second_col': sc})

