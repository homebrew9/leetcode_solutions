-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


# MySQL
# Write your MySQL query statement below
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


# Pandas

