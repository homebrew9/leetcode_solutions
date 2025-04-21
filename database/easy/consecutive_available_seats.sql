-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select seat_id, free,
           lag(free) over (order by seat_id) as prev_seat_id,
           lead(free) over (order by seat_id) as next_seat_id
      from cinema
)
select seat_id
  from t
 where free = 1
   and (coalesce(next_seat_id, 0) = 1 or coalesce(prev_seat_id, 0) = 1)
 order by seat_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select seat_id, free,
           lag(free) over (order by seat_id) as prev_seat_id,
           lead(free) over (order by seat_id) as next_seat_id
      from cinema
)
select seat_id
  from t
 where free = 1
   and (coalesce(next_seat_id, 0) = 1 or coalesce(prev_seat_id, 0) = 1)
 order by seat_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select seat_id, free,
           lag(free) over (order by seat_id) as prev_seat_id,
           lead(free) over (order by seat_id) as next_seat_id
      from cinema
)
select seat_id
  from t
 where free = 1
   and (coalesce(next_seat_id, 0) = 1 or coalesce(prev_seat_id, 0) = 1)
 order by seat_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select seat_id, free,
           lag(free) over (order by seat_id) as prev_seat_id,
           lead(free) over (order by seat_id) as next_seat_id
      from cinema
)
select seat_id
  from t
 where free = 1
   and (coalesce(next_seat_id, 0) = 1 or coalesce(prev_seat_id, 0) = 1)
 order by seat_id
;


# Pandas
import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema['lag'] = cinema.shift(1)['free']
    cinema['lead'] = cinema.shift(-1)['free']
    return cinema.query('free != 0 and (lag==1 or lead==1)')[['seat_id']].sort_values(by=['seat_id'])

