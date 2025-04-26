-- Oracle
/* Write your PL/SQL query statement below */
select *
from (select id, revenue, month from department)
pivot (
    max(revenue)
    for month in (
        'Jan' as "Jan_Revenue",
        'Feb' as "Feb_Revenue",
        'Mar' as "Mar_Revenue",
        'Apr' as "Apr_Revenue",
        'May' as "May_Revenue",
        'Jun' as "Jun_Revenue",
        'Jul' as "Jul_Revenue",
        'Aug' as "Aug_Revenue",
        'Sep' as "Sep_Revenue",
        'Oct' as "Oct_Revenue",
        'Nov' as "Nov_Revenue",
        'Dec' as "Dec_Revenue"
    )
)
order by id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select id,
       max(case when month = 'Jan' then revenue end) as Jan_Revenue,
       max(case when month = 'Feb' then revenue end) as Feb_Revenue,
       max(case when month = 'Mar' then revenue end) as Mar_Revenue,
       max(case when month = 'Apr' then revenue end) as Apr_Revenue,
       max(case when month = 'May' then revenue end) as May_Revenue,
       max(case when month = 'Jun' then revenue end) as Jun_Revenue,
       max(case when month = 'Jul' then revenue end) as Jul_Revenue,
       max(case when month = 'Aug' then revenue end) as Aug_Revenue,
       max(case when month = 'Sep' then revenue end) as Sep_Revenue,
       max(case when month = 'Oct' then revenue end) as Oct_Revenue,
       max(case when month = 'Nov' then revenue end) as Nov_Revenue,
       max(case when month = 'Dec' then revenue end) as Dec_Revenue
  from department
 group by id
;


-- SQL Server
/* Write your T-SQL query statement below */
select id,
       max(case when month = 'Jan' then revenue end) as Jan_Revenue,
       max(case when month = 'Feb' then revenue end) as Feb_Revenue,
       max(case when month = 'Mar' then revenue end) as Mar_Revenue,
       max(case when month = 'Apr' then revenue end) as Apr_Revenue,
       max(case when month = 'May' then revenue end) as May_Revenue,
       max(case when month = 'Jun' then revenue end) as Jun_Revenue,
       max(case when month = 'Jul' then revenue end) as Jul_Revenue,
       max(case when month = 'Aug' then revenue end) as Aug_Revenue,
       max(case when month = 'Sep' then revenue end) as Sep_Revenue,
       max(case when month = 'Oct' then revenue end) as Oct_Revenue,
       max(case when month = 'Nov' then revenue end) as Nov_Revenue,
       max(case when month = 'Dec' then revenue end) as Dec_Revenue
  from department
 group by id
;


# MySQL
# Write your MySQL query statement below
select id,
       max(case when month = 'Jan' then revenue end) as Jan_Revenue,
       max(case when month = 'Feb' then revenue end) as Feb_Revenue,
       max(case when month = 'Mar' then revenue end) as Mar_Revenue,
       max(case when month = 'Apr' then revenue end) as Apr_Revenue,
       max(case when month = 'May' then revenue end) as May_Revenue,
       max(case when month = 'Jun' then revenue end) as Jun_Revenue,
       max(case when month = 'Jul' then revenue end) as Jul_Revenue,
       max(case when month = 'Aug' then revenue end) as Aug_Revenue,
       max(case when month = 'Sep' then revenue end) as Sep_Revenue,
       max(case when month = 'Oct' then revenue end) as Oct_Revenue,
       max(case when month = 'Nov' then revenue end) as Nov_Revenue,
       max(case when month = 'Dec' then revenue end) as Dec_Revenue
  from department
 group by id
;


# Pandas
import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table to have months as columns
    department = department.pivot(index='id', columns='month', values='revenue')
    all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    department = department.reindex(columns=all_months)
    department.columns = [f"{month}_Revenue" for month in department.columns]
    department = department.reset_index()
    return department

