-- Oracle
/* Write your PL/SQL query statement below */
--
with t (player_id, device_id, event_date, games_played, first_login_date) as (
select player_id, device_id, event_date, games_played,
       min(event_date) over (partition by player_id) as first_login_date
from activity
),
t1 (player_count_consecutive) as (
select count(distinct player_id)
from t
where event_date = first_login_date + 1
),
t2 (player_count_total) as (
select count(distinct player_id) as player_count from activity
)
select round(t1.player_count_consecutive / t2.player_count_total, 2) as fraction
from t1 cross join t2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (total_players) as (
    select count(distinct player_id)
      from activity
),
t1 (player_id, first_login) as (
    select player_id, min(event_date)
      from activity
     group by player_id
),
t2 (returning_player_count) as (
    select count(distinct a.player_id)
      from activity a
           inner join t1 on (t1.player_id = a.player_id and t1.first_login = a.event_date - interval '1 day')
)
select round(t2.returning_player_count::numeric / t.total_players, 2) as fraction
  from t2
       cross join t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (total_players) as (
    select count(distinct player_id)
      from activity
),
t1 (player_id, first_login) as (
    select player_id, min(event_date)
      from activity
     group by player_id
),
t2 (returning_player_count) as (
    select count(distinct a.player_id)
      from activity a
           inner join t1 on (t1.player_id = a.player_id and dateadd(day, 1, t1.first_login) = a.event_date)
)
select round(convert(float, t2.returning_player_count) / t.total_players, 2) as fraction
  from t2
       cross join t
;


# MySQL
# Write your MySQL query statement below
with t (total_players) as (
    select count(distinct player_id)
      from activity
),
t1 (player_id, first_login) as (
    select player_id, min(event_date)
      from activity
     group by player_id
),
t2 (returning_player_count) as (
    select count(distinct a.player_id)
      from activity a
           inner join t1 on (t1.player_id = a.player_id and t1.first_login = date_sub(a.event_date, interval 1 day))
)
select round(t2.returning_player_count / t.total_players, 2) as fraction
  from t2
       cross join t
;


# Pandas


