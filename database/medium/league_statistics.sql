-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


# MySQL
# Write your MySQL query statement below
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


# Pandas

