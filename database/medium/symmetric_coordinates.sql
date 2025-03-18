-- Oracle
/* Write your PL/SQL query statement below */
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y from t1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


# MySQL
# Write your MySQL query statement below
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


# Pandas

