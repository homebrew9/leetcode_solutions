-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (seat_id, free, grp) as (
    select seat_id, free,
           case when lag(free) over (order by seat_id) != free then 1 else 0
           end as grp
      from cinema
),
t1 as (
    select seat_id, free, grp,
           sum(grp) over (order by seat_id) as group_id
    from t
),
t2 (group_id, first_seat_id, last_seat_id, consecutive_seats_len) as (
    select group_id, min(seat_id), max(seat_id), count(*)
      from t1
     where free = 1
     group by group_id
)
select first_seat_id, last_seat_id, consecutive_seats_len
  from t2
 where consecutive_seats_len = (select max(consecutive_seats_len) from t2)
 order by first_seat_id
;


-- SQL Server


# MySQL


# Pandas

