-- Oracle
/* Write your PL/SQL query statement below */
with t (company_id, employee_id, employee_name, salary, max_company_salary) as (
select company_id, employee_id, employee_name, salary,
       max(salary) over (partition by company_id) as max_company_salary
from salaries
)
select company_id, employee_id, employee_name,
       round(case when max_company_salary between 1000 and 10000 then salary * (1 - 0.24)
                  when max_company_salary > 10000 then salary * (1 - 0.49)
                  else salary
             end) as salary
from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (company_id, employee_id, employee_name, salary, max_company_salary) as (
select company_id, employee_id, employee_name, salary,
       max(salary) over (partition by company_id) as max_company_salary
from salaries
)
select company_id, employee_id, employee_name,
       round(case when max_company_salary between 1000 and 10000 then salary * (1 - 0.24)
                  when max_company_salary > 10000 then salary * (1 - 0.49)
                  else salary
             end) as salary
from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (company_id, employee_id, employee_name, salary, max_company_salary) as (
select company_id, employee_id, employee_name, salary,
       max(salary) over (partition by company_id) as max_company_salary
from salaries
)
select company_id, employee_id, employee_name,
       round(case when max_company_salary between 1000 and 10000 then salary * (1 - 0.24)
                  when max_company_salary > 10000 then salary * (1 - 0.49)
                  else salary
             end, 0) as salary
from t
;


# MySQL
# Write your MySQL query statement below
with t (company_id, employee_id, employee_name, salary, max_company_salary) as (
select company_id, employee_id, employee_name, salary,
       max(salary) over (partition by company_id) as max_company_salary
from salaries
)
select company_id, employee_id, employee_name,
       round(case when max_company_salary between 1000 and 10000 then salary * (1 - 0.24)
                  when max_company_salary > 10000 then salary * (1 - 0.49)
                  else salary
             end) as salary
from t
;


# Pandas
import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:
    df = salaries.groupby('company_id',as_index=False)['salary'].max()
    df['tax'] = np.where(df['salary']>10000,1-0.49, np.where(df['salary']<1000, 1, 1-0.24))
    salaries = (salaries.merge(df, how='left', on='company_id')
                        .rename(columns={'salary_x':'salary', 'salary_y':'company_max_salary'})
               )
    # What I understood - rounding correctly is difficult! Python's round() function rounds to nearest even number!
    # Adding 0.5 and converting to int is a hack.
    salaries['after_tax'] = (salaries['salary']*salaries['tax']+0.5).astype(int)
    return salaries[['company_id','employee_id','employee_name','after_tax']].rename(columns={'after_tax':'salary'})

