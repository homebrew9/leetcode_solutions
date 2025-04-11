-- Oracle
/* Write your PL/SQL query statement below */
select x.weekend_cnt, y.working_cnt
from (select count(*) as weekend_cnt from tasks where to_char(submit_date,'Dy') in ('Sat','Sun')) x
     cross join
     (select count(*) as working_cnt from tasks where to_char(submit_date,'Dy') not in ('Sat','Sun')) y
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select x.weekend_cnt, y.working_cnt
from (select count(*) as weekend_cnt from tasks where to_char(submit_date,'Dy') in ('Sat','Sun')) x
     cross join
     (select count(*) as working_cnt from tasks where to_char(submit_date,'Dy') not in ('Sat','Sun')) y
;


-- SQL Server
/* Write your T-SQL query statement below */
select x.weekend_cnt, y.working_cnt
from (select count(*) as weekend_cnt from tasks where datename(weekday, submit_date) in ('Saturday','Sunday')) x
     cross join
     (select count(*) as working_cnt from tasks where datename(weekday, submit_date) not in ('Saturday','Sunday')) y
;


# MySQL
# Write your MySQL query statement below
-- dayofweek(now()) returns [1..7] where 1=Sunday, 2=Monday,... 7=Saturday
select x.weekend_cnt, y.working_cnt
from (select count(*) as weekend_cnt from tasks where dayofweek(submit_date) in (1,7)) x
     cross join
     (select count(*) as working_cnt from tasks where dayofweek(submit_date) not in (1,7)) y
;


# Pandas
import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    return (  pd.DataFrame(data={'weekend_cnt': len(tasks[tasks['submit_date'].dt.dayofweek.isin([5,6])]),
                                 'working_cnt': len(tasks[~tasks['submit_date'].dt.dayofweek.isin([5,6])])
                                },
                           index=[0]
                          )
    )

