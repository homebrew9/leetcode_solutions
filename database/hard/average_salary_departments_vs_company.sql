-- Oracle
/* Write your PL/SQL query statement below */
with t (pay_month, department_id, amount, avg_dept_salary, avg_comp_salary) as (
select to_char(s.pay_date, 'YYYY-MM') as pay_month, e.department_id, s.amount,
       avg(s.amount) over (partition by to_char(s.pay_date, 'YYYY-MM'), e.department_id) as avg_dept_salary,
       avg(s.amount) over (partition by to_char(s.pay_date, 'YYYY-MM')) as avg_comp_salary
from salary s
     inner join employee e on (e.employee_id = s.employee_id)
)
select distinct pay_month,
       department_id,
       case when avg_dept_salary > avg_comp_salary then 'higher'
            when avg_dept_salary < avg_comp_salary then 'lower'
            else 'same'
       end as comparison
from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (pay_date, department_id, amount, avg_dept_salary, avg_comp_salary) as (
select date_trunc('month', s.pay_date) as pay_date, e.department_id, s.amount,
       avg(s.amount) over (partition by date_trunc('month', s.pay_date), e.department_id) as avg_dept_salary,
       avg(s.amount) over (partition by date_trunc('month', s.pay_date)) as avg_comp_salary
from salary s
     inner join employee e on (e.employee_id = s.employee_id)
)
select distinct to_char(pay_date, 'YYYY-MM') as pay_month,
       department_id,
       case when avg_dept_salary > avg_comp_salary then 'higher'
            when avg_dept_salary < avg_comp_salary then 'lower'
            else 'same'
       end as comparison
from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (pay_month, department_id, amount, avg_dept_salary, avg_comp_salary) as (
select left(convert(varchar, s.pay_date, 23), 7) as pay_month, e.department_id, s.amount,
       avg(s.amount) over (partition by left(convert(varchar, s.pay_date, 23), 7), e.department_id) as avg_dept_salary,
       avg(s.amount) over (partition by left(convert(varchar, s.pay_date, 23), 7)) as avg_comp_salary
from salary s
     inner join employee e on (e.employee_id = s.employee_id)
)
select distinct pay_month,
       department_id,
       case when avg_dept_salary > avg_comp_salary then 'higher'
            when avg_dept_salary < avg_comp_salary then 'lower'
            else 'same'
       end as comparison
from t
;


# MySQL
# Write your MySQL query statement below
with t as (
select distinct date_format(s.pay_date, '%Y-%m') as pay_month, e.department_id,
       avg(s.amount) over (partition by date_format(s.pay_date, '%Y-%m')) as cmp_avg,
       avg(s.amount) over (partition by date_format(s.pay_date, '%Y-%m'), e.department_id) as dpt_avg
from salary s
     inner join employee e on (e.employee_id = s.employee_id)
)
select pay_month, department_id,
       case when dpt_avg > cmp_avg then 'higher'
            when dpt_avg < cmp_avg then 'lower'
            else 'same'
       end as comparison
  from t
;


# Pandas
import pandas as pd

def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = salary.merge(employee, how='inner', on='employee_id')
    df['pay_month'] = df['pay_date'].dt.strftime('%Y-%m')
    avg_comp_salary = df.groupby('pay_month', as_index=False)['amount'].mean()
    avg_dept_salary = df.groupby(['pay_month','department_id'], as_index=False)['amount'].mean()
    df = avg_dept_salary.merge(avg_comp_salary, how='left', on='pay_month')
    df['comparison'] = ( np.where(
                             df['amount_x'] > df['amount_y'],
                             'higher',
                             np.where(
                                 df['amount_x'] < df['amount_y'],
                                 'lower',
                                 'same'
                             )
                         )
                       )
    return df[['pay_month','department_id','comparison']]

