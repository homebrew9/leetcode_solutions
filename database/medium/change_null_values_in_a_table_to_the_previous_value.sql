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
-- Write your PostgreSQL query statement below
with t (id, drink, rnum) as (
    select id, drink, row_number() over () as rnum
      from coffeeshop
),
consolidated (id, drink, rnum, max_t2_rnum) as (
    select t1.id, t1.drink, t1.rnum, max(t2.rnum) as max_t2_rnum
      from t t1
             left outer join t t2 on (t2.rnum < t1.rnum and t2.drink is not null)
     group by t1.id, t1.drink, t1.rnum
)
select c.id, coalesce(c.drink, t.drink) as drink
  from consolidated c
       left outer join t on (t.rnum = c.max_t2_rnum)
 order by c.rnum
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (id, drink, rnum) as (
    select id, drink, row_number() over (order by (select null)) as rnum
      from coffeeshop
),
consolidated (id, drink, rnum, max_t2_rnum) as (
    select t1.id, t1.drink, t1.rnum, max(t2.rnum) as max_t2_rnum
      from t t1
             left outer join t t2 on (t2.rnum < t1.rnum and t2.drink is not null)
     group by t1.id, t1.drink, t1.rnum
)
select c.id, coalesce(c.drink, t.drink) as drink
  from consolidated c
       left outer join t on (t.rnum = c.max_t2_rnum)
 order by c.rnum
;


# MySQL
# Write your MySQL query statement below
with t (id, drink, rnum) as (
    select id, drink, row_number() over () as rnum
      from coffeeshop
),
consolidated (id, drink, rnum, max_t2_rnum) as (
    select t1.id, t1.drink, t1.rnum, max(t2.rnum) as max_t2_rnum
      from t t1
             left outer join t t2 on (t2.rnum < t1.rnum and t2.drink is not null)
     group by t1.id, t1.drink, t1.rnum
)
select c.id, coalesce(c.drink, t.drink) as drink
  from consolidated c
       left outer join t on (t.rnum = c.max_t2_rnum)
 order by c.rnum
;


# Pandas

