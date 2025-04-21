-- Oracle
/* Write your PL/SQL query statement below */
select extra as report_reason,
       count(distinct post_id) as report_count
from actions
where action_date = DATE'2019-07-04'
and extra is not null
and action = 'report'
group by extra
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select extra as report_reason,
       count(distinct post_id) as report_count
from actions
where action_date = '2019-07-04'
and extra is not null
and action = 'report'
group by extra
;


-- SQL Server
/* Write your T-SQL query statement below */
select extra as report_reason,
       count(distinct post_id) as report_count
from actions
where action_date = '2019-07-04'
and extra is not null
and action = 'report'
group by extra
;


# MySQL
# Write your MySQL query statement below
select extra as report_reason,
       count(distinct post_id) as report_count
from actions
where action_date = '2019-07-04'
and extra is not null
and action = 'report'
group by extra
;


# Pandas
import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    return (
             actions.query("action == 'report' and action_date == '2019-07-04'")[['post_id','extra']]
                    .drop_duplicates()
                    .groupby('extra',as_index=False)['post_id']
                    .count()
                    .rename(columns={'extra':'report_reason', 'post_id':'report_count'})
           )

