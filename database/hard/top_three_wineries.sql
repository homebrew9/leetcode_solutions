-- Oracle
/* Write your PL/SQL query statement below */
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then winery||' ('||total_points||')' else null end) as top_winery,
       nvl(max(case when drnk = 2 then winery||' ('||total_points||')' else null end), 'No second winery') as second_winery,
       nvl(max(case when drnk = 3 then winery||' ('||total_points||')' else null end), 'No third winery') as third_winery
from t1
group by country
order by country
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then winery+' ('+convert(varchar,total_points)+')' else null end) as top_winery,
       isnull(
           max(case when drnk = 2 then winery+' ('+convert(varchar,total_points)+')' else null end),
           'No second winery'
       ) as second_winery,
       isnull(
           max(case when drnk = 3 then winery+' ('+convert(varchar,total_points)+')' else null end),
           'No third winery'
       ) as third_winery
from t1
group by country
order by country
;


# MySQL
# Write your MySQL query statement below
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then concat(winery,' (',total_points,')') else null end) as top_winery,
       coalesce(
           max(case when drnk = 2 then concat(winery,' (',total_points,')') else null end),
           'No second winery'
       ) as second_winery,
       coalesce(
           max(case when drnk = 3 then concat(winery,' (',total_points,')') else null end),
           'No third winery'
       ) as third_winery
from t1
group by country
order by country
;


# Pandas

