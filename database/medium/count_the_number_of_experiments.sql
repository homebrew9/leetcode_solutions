-- Oracle
/* Write your PL/SQL query statement below */
with platform_experiment as (
    select x.platform, y.experiment_name
    from (  select 'Android' as platform from dual union all
            select 'IOS' from dual union all
            select 'Web' from dual
         ) x
         cross join (
             select 'Reading' as experiment_name from dual union all
             select 'Sports' from dual union all
             select 'Programming' from dual
         ) y
)
select pe.platform, pe.experiment_name,
       coalesce(e.num_experiments, 0) as num_experiments
from platform_experiment pe
     left outer join (
                        select platform, experiment_name, count(*) as num_experiments
                          from experiments
                         group by platform, experiment_name
                     ) e
     on (e.platform = pe.platform and e.experiment_name = pe.experiment_name)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with platform_experiment as (
    select x.platform, y.experiment_name
    from (  select 'Android' as platform union all
            select 'IOS' union all
            select 'Web'
         ) x
         cross join (
             select 'Reading' as experiment_name union all
             select 'Sports' union all
             select 'Programming'
         ) y
)
select pe.platform, pe.experiment_name,
       coalesce(e.num_experiments, 0) as num_experiments
from platform_experiment pe
     left outer join (
                        select platform, experiment_name, count(*) as num_experiments
                          from experiments
                         group by platform, experiment_name
                     ) e
     on (e.platform = pe.platform and e.experiment_name = pe.experiment_name)
;


-- SQL Server
/* Write your T-SQL query statement below */
with platform_experiment as (
    select x.platform, y.experiment_name
    from (  select 'Android' as platform union all
            select 'IOS' union all
            select 'Web'
         ) x
         cross join (
             select 'Reading' as experiment_name union all
             select 'Sports' union all
             select 'Programming'
         ) y
)
select pe.platform, pe.experiment_name,
       coalesce(e.num_experiments, 0) as num_experiments
from platform_experiment pe
     left outer join (
                        select platform, experiment_name, count(*) as num_experiments
                          from experiments
                         group by platform, experiment_name
                     ) e
     on (e.platform = pe.platform and e.experiment_name = pe.experiment_name)
;


# MySQL
# Write your MySQL query statement below
with platform_experiment as (
    select x.platform, y.experiment_name
    from (  select 'Android' as platform union all
            select 'IOS' union all
            select 'Web'
         ) x
         cross join (
             select 'Reading' as experiment_name union all
             select 'Sports' union all
             select 'Programming'
         ) y
)
select pe.platform, pe.experiment_name,
       coalesce(e.num_experiments, 0) as num_experiments
from platform_experiment pe
     left outer join (
                        select platform, experiment_name, count(*) as num_experiments
                          from experiments
                         group by platform, experiment_name
                     ) e
     on (e.platform = pe.platform and e.experiment_name = pe.experiment_name)
;


# Pandas

