-- Oracle
/* Write your PL/SQL query statement below */
select e.reports_to as employee_id, e1.name, count(*) as reports_count, round(avg(e.age)) as average_age
from employees e
     inner join employees e1 on (e1.employee_id = e.reports_to)
group by e.reports_to, e1.name
order by e.reports_to
;

/* Write your PL/SQL query statement below */
with t_manager (employee_id, name) as (
select x.employee_id, x.name
from employees x
where x.employee_id in (select y.reports_to from employees y where y.reports_to is not null)
)
select m.employee_id, m.name, count(*) as reports_count, round(avg(e.age)) as average_age
from t_manager m
     inner join employees e on (m.employee_id = e.reports_to)
group by m.employee_id, m.name
order by m.employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e1.reports_to as employee_id,
       e2.name,
       count(e1.employee_id) as reports_count,
       round(avg(e1.age)) as average_age
  from employees e1
       inner join employees e2 on (e2.employee_id = e1.reports_to)
 group by e1.reports_to, e2.name
 order by e1.reports_to
;


-- SQL Server
/* Write your T-SQL query statement below */
select e1.reports_to as employee_id,
       e2.name,
       count(e1.employee_id) as reports_count,
       round(avg(convert(float, e1.age)), 0) as average_age
  from employees e1
       inner join employees e2 on (e2.employee_id = e1.reports_to)
 group by e1.reports_to, e2.name
 order by e1.reports_to
;


# MySQL
# Write your MySQL query statement below
select e1.reports_to as employee_id,
       e2.name,
       count(e1.employee_id) as reports_count,
       round(avg(e1.age)) as average_age
  from employees e1
       inner join employees e2 on (e2.employee_id = e1.reports_to)
 group by e1.reports_to, e2.name
 order by e1.reports_to
;


# Pandas
import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = ( employees
          .groupby('reports_to', as_index=0)
          .agg(reports_count=('employee_id', 'count'), average_age=('age', 'mean'))
          .rename(columns={'reports_to': 'employee_id'})
         )
    # The lambda function is the alternative to Python's "Banker's rounding"
    df['average_age'] = df['average_age'].apply(lambda x: int(x + 0.5))
    return ( df
            .merge(employees, how='inner', on='employee_id')[['employee_id', 'name', 'reports_count', 'average_age']]
            .sort_values('employee_id')
           )

