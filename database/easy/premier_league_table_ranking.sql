-- Oracle
/* Write your PL/SQL query statement below */
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


# MySQL
# Write your MySQL query statement below
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


# Pandas

