-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, b.capacity, count(p.passenger_id) as passenger_cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time, b.capacity
),
t1 as (
select bus_id, arrival_time, capacity, passenger_cnt,
       passenger_cnt - coalesce(lag(passenger_cnt) over (order by arrival_time), 0) as delta_cnt,
       row_number() over (order by arrival_time) as rn
from t
),
t2 (bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn, boarded, leftover) as (
    select bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn,
           least(capacity, passenger_cnt),
           delta_cnt - least(capacity, passenger_cnt)
    from t1
    where rn = 1
    union all
    select t1.bus_id, t1.arrival_time, t1.capacity, t1.passenger_cnt, t1.delta_cnt, t1.rn,
           least(t1.capacity, t1.delta_cnt + t2.leftover),
           (t1.delta_cnt + t2.leftover) - least(t1.capacity, t1.delta_cnt + t2.leftover)
    from t1 inner join t2 on (t1.rn = t2.rn + 1)
)
select bus_id, boarded as passengers_cnt
from t2
order by bus_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t as (
select b.bus_id, b.arrival_time, b.capacity, count(p.passenger_id) as passenger_cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time, b.capacity
),
t1 as (
select bus_id, arrival_time, capacity, passenger_cnt,
       passenger_cnt - coalesce(lag(passenger_cnt) over (order by arrival_time), 0) as delta_cnt,
       row_number() over (order by arrival_time) as rn
from t
),
t2 (bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn, boarded, leftover) as (
    select bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn,
           least(capacity, passenger_cnt),
           delta_cnt - least(capacity, passenger_cnt)
    from t1
    where rn = 1
    union all
    select t1.bus_id, t1.arrival_time, t1.capacity, t1.passenger_cnt, t1.delta_cnt, t1.rn,
           least(t1.capacity, t1.delta_cnt + t2.leftover),
           (t1.delta_cnt + t2.leftover) - least(t1.capacity, t1.delta_cnt + t2.leftover)
    from t1 inner join t2 on (t1.rn = t2.rn + 1)
)
select bus_id, boarded as passengers_cnt
from t2
order by bus_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, b.capacity, count(p.passenger_id) as passenger_cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time, b.capacity
),
t1 as (
select bus_id, arrival_time, capacity, passenger_cnt,
       passenger_cnt - coalesce(lag(passenger_cnt) over (order by arrival_time), 0) as delta_cnt,
       row_number() over (order by arrival_time) as rn
from t
),
t2 (bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn, boarded, leftover) as (
    select bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn,
           --least(capacity, passenger_cnt),
           case when capacity <= passenger_cnt
                then capacity
                else passenger_cnt
           end,
           --delta_cnt - least(capacity, passenger_cnt)
           delta_cnt
           - case when capacity <= passenger_cnt
                  then capacity
                  else passenger_cnt
             end
    from t1
    where rn = 1
    union all
    select t1.bus_id, t1.arrival_time, t1.capacity, t1.passenger_cnt, t1.delta_cnt, t1.rn,
           --least(t1.capacity, t1.delta_cnt + t2.leftover),
           case when t1.capacity <= t1.delta_cnt + t2.leftover
                then t1.capacity
                else t1.delta_cnt + t2.leftover
           end,
           --(t1.delta_cnt + t2.leftover) - least(t1.capacity, t1.delta_cnt + t2.leftover)
           (t1.delta_cnt + t2.leftover)
           - case when t1.capacity <= t1.delta_cnt + t2.leftover
                  then t1.capacity
                  else t1.delta_cnt + t2.leftover
             end
    from t1 inner join t2 on (t1.rn = t2.rn + 1)
)
select bus_id, boarded as passengers_cnt
from t2
order by bus_id
;


# MySQL
# Write your MySQL query statement below
with recursive t as (
select b.bus_id, b.arrival_time, b.capacity, count(p.passenger_id) as passenger_cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time, b.capacity
),
t1 as (
select bus_id, arrival_time, capacity, passenger_cnt,
       passenger_cnt - coalesce(lag(passenger_cnt) over (order by arrival_time), 0) as delta_cnt,
       row_number() over (order by arrival_time) as rn
from t
),
t2 (bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn, boarded, leftover) as (
    select bus_id, arrival_time, capacity, passenger_cnt, delta_cnt, rn,
           least(capacity, passenger_cnt),
           delta_cnt - least(capacity, passenger_cnt)
    from t1
    where rn = 1
    union all
    select t1.bus_id, t1.arrival_time, t1.capacity, t1.passenger_cnt, t1.delta_cnt, t1.rn,
           least(t1.capacity, t1.delta_cnt + t2.leftover),
           (t1.delta_cnt + t2.leftover) - least(t1.capacity, t1.delta_cnt + t2.leftover)
    from t1 inner join t2 on (t1.rn = t2.rn + 1)
)
select bus_id, boarded as passengers_cnt
from t2
order by bus_id
;

