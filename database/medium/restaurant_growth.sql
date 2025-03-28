-- Oracle
/* Write your PL/SQL query statement below */
with t (visited_on, amount) as (
    select visited_on, sum(amount) as amount
      from Customer
     group by visited_on
),
t1 (visited_on, amount, rnum) as (
    select visited_on, amount, row_number() over (order by visited_on) as rnum
      from t
),
t2 (visited_on, rnum, amount, average_amount) as (
select to_char(visited_on, 'YYYY-MM-DD') as visited_on,
       rnum,
       round(sum(amount) over (order by visited_on rows between 6 preceding and current row),2) as amount,
       round(avg(amount) over (order by visited_on rows between 6 preceding and current row),2) as average_amount
  from t1
)
select visited_on, amount, average_amount
from t2
where rnum >= 7
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (visited_on, amount) as (
    select visited_on, sum(amount) as amount
      from customer
     group by visited_on
),
t1 (visited_on, amount, rnum) as (
    select visited_on, amount, row_number() over (order by visited_on) as rnum
      from t
),
t2 (visited_on, rnum, amount, average_amount) as (
    select visited_on, rnum,
           round(sum(amount) over (order by rnum rows between 6 preceding and current row), 2) as amount,
           round(avg(amount) over (order by rnum rows between 6 preceding and current row), 2) as average_amount
      from t1
)
select visited_on, amount, average_amount
  from t2
 where rnum >= 7
 order by rnum
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (visited_on, amount) as (
    select visited_on, sum(amount) as amount
      from customer
     group by visited_on
),
t1 (visited_on, amount, rnum) as (
    select visited_on, convert(float, amount), row_number() over (order by visited_on) as rnum
      from t
),
t2 (visited_on, rnum, amount, average_amount) as (
    select visited_on, rnum,
           round(sum(amount) over (order by rnum rows between 6 preceding and current row), 2) as amount,
           round(avg(amount) over (order by rnum rows between 6 preceding and current row), 2) as average_amount
      from t1
)
select visited_on, amount, average_amount
  from t2
 where rnum >= 7
 order by rnum
;

# MySQL


# Pandas

