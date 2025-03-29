-- Oracle
/* Write your PL/SQL query statement below */
with t (seat_id, free, root_node) as (
    select seat_id, free,
           case
               when free = 1 and coalesce(lag(free) over (order by seat_id), 0) = 0
               then 1
           end as root_node
      from cinema
),
t_hier (first_seat_id, last_seat_id, seat_length) as (
    select t.seat_id, t.seat_id, 1
      from t
     where t.root_node = 1
    union all
    select t_hier.first_seat_id, t.seat_id, t_hier.seat_length + 1
      from t_hier
           inner join t on (t.seat_id = t_hier.last_seat_id + 1 and t.free = 1)
),
t1 as (
    select first_seat_id, max(last_seat_id) as last_seat_id,
           max(seat_length) as consecutive_seats_len
      from t_hier
     group by first_seat_id
)
select first_seat_id, last_seat_id, consecutive_seats_len
  from t1
 where t1.consecutive_seats_len = (select max(consecutive_seats_len)
                                    from t1
                                 )
 order by first_seat_id
;


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
/* Write your T-SQL query statement below */
with t (seat_id, free, root_node) as (
    select seat_id, free,
           case
               when free = 1 and coalesce(lag(free) over (order by seat_id), 0) = 0
               then 1
           end as root_node
      from cinema
),
t_hier (first_seat_id, last_seat_id, seat_length) as (
    select t.seat_id, t.seat_id, 1
      from t
     where t.root_node = 1
    union all
    select t_hier.first_seat_id, t.seat_id, t_hier.seat_length + 1
      from t_hier
           inner join t on (t.seat_id = t_hier.last_seat_id + 1 and t.free = 1)
),
t1 as (
    select first_seat_id, max(last_seat_id) as last_seat_id,
           max(seat_length) as consecutive_seats_len
      from t_hier
     group by first_seat_id
)
select first_seat_id, last_seat_id, consecutive_seats_len
  from t1
 where t1.consecutive_seats_len = (select max(consecutive_seats_len)
                                    from t1
                                 )
 order by first_seat_id
;


# MySQL
# Write your MySQL query statement below
with recursive t (seat_id, free, root_node) as (
    select seat_id, free,
           case
               when free = 1 and coalesce(lag(free) over (order by seat_id), 0) = 0
               then 1
           end as root_node
      from cinema
),
t_hier (first_seat_id, last_seat_id, seat_length) as (
    select t.seat_id, t.seat_id, 1
      from t
     where t.root_node = 1
    union all
    select t_hier.first_seat_id, t.seat_id, t_hier.seat_length + 1
      from t_hier
           inner join t on (t.seat_id = t_hier.last_seat_id + 1 and t.free = 1)
),
t1 as (
    select first_seat_id, max(last_seat_id) as last_seat_id,
           max(seat_length) as consecutive_seats_len
      from t_hier
     group by first_seat_id
)
select first_seat_id, last_seat_id, consecutive_seats_len
  from t1
 where t1.consecutive_seats_len = (select max(consecutive_seats_len)
                                    from t1
                                 )
 order by first_seat_id
;


# Pandas
import pandas as pd

def consecutive_available_seats(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema['prev'] = cinema['free'].shift(1)
    cinema['marker'] = np.where(cinema['free'] != cinema['prev'], 1, 0)
    cinema['group_id'] = cinema['marker'].cumsum()
    df = ( cinema[cinema['free'] == 1]
          .groupby('group_id', as_index=0)['seat_id']
          .agg(first_seat_id='min', last_seat_id='max', consecutive_seats_len='count')
         )
    return ( df[df['consecutive_seats_len'] == df['consecutive_seats_len'].max()]
            .sort_values('first_seat_id')[['first_seat_id','last_seat_id','consecutive_seats_len']]
           )

