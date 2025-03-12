-- Oracle
/* Write your PL/SQL query statement below */
with t (ceo_id, ceo_salary) as (
    select employee_id, salary
      from employees
     where manager_id is null
)
select e.employee_id as subordinate_id,
       e.employee_name as subordinate_name,
       level as hierarchy_level,
       e.salary - t.ceo_salary as salary_difference
  from employees e
       cross join t
 start with e.manager_id = t.ceo_id
connect by e.manager_id = prior e.employee_id
order by hierarchy_level, subordinate_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (employee_id, employee_name, depth, ceo_salary, diff) as (
    select employee_id, employee_name, 0, salary, 0
      from employees
     where manager_id is null
    union all
    select e.employee_id, e.employee_name, t.depth + 1, t.ceo_salary, e.salary - t.ceo_salary
      from employees e
           inner join t on (e.manager_id = t.employee_id)
)
select employee_id as subordinate_id,
       employee_name as subordinate_name,
       depth as hierarchy_level,
       diff as salary_difference
  from t
 where t.depth > 0
 order by hierarchy_level, subordinate_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (employee_id, employee_name, depth, ceo_salary, diff) as (
    select employee_id, employee_name, 0, salary, 0
      from employees
     where manager_id is null
    union all
    select e.employee_id, e.employee_name, t.depth + 1, t.ceo_salary, e.salary - t.ceo_salary
      from employees e
           inner join t on (e.manager_id = t.employee_id)
)
select employee_id as subordinate_id,
       employee_name as subordinate_name,
       depth as hierarchy_level,
       diff as salary_difference
  from t
 where t.depth > 0
 order by hierarchy_level, subordinate_id
;


# MySQL
# Write your MySQL query statement below
with recursive t (employee_id, employee_name, depth, ceo_salary, diff) as (
    select employee_id, employee_name, 0, salary, 0
      from employees
     where manager_id is null
    union all
    select e.employee_id, e.employee_name, t.depth + 1, t.ceo_salary, e.salary - t.ceo_salary
      from employees e
           inner join t on (e.manager_id = t.employee_id)
)
select employee_id as subordinate_id,
       employee_name as subordinate_name,
       depth as hierarchy_level,
       diff as salary_difference
  from t
 where t.depth > 0
 order by hierarchy_level, subordinate_id
;


# Pandas
import pandas as pd

def find_subordinates(employees: pd.DataFrame) -> pd.DataFrame:
    ceo_df = employees[employees['manager_id'].isna()]
    ceo_id = ceo_df['employee_id'][0]
    ceo_salary = ceo_df['salary'][0]
    subordinates = employees.loc[0:-1]
    subordinates['level'] = None
    subordinates['diff'] = None
    base_df = employees[employees['employee_id'] == ceo_id]
    level = 0
    while True:
        temp_df = ( employees
                   .merge(base_df,
                          how='inner',
                          left_on='manager_id',
                          right_on='employee_id'
                         )[['employee_id_x','employee_name_x','manager_id_x','salary_x']]
                   .rename(columns={'employee_id_x':'employee_id',
                                    'employee_name_x':'employee_name',
                                    'manager_id_x':'manager_id',
                                    'salary_x':'salary' })
                  )
        if len(temp_df) == 0:
            break
        level += 1
        temp_df['level'] = level
        temp_df['diff'] = temp_df['salary'] - ceo_salary
        subordinates = pd.concat([subordinates, temp_df])
        base_df = temp_df
    subordinates = subordinates[['employee_id','employee_name','level','diff']]
    subordinates = ( subordinates
                    .rename(columns={'employee_id': 'subordinate_id',
                                     'employee_name': 'subordinate_name',
                                     'level': 'hierarchy_level',
                                     'diff': 'salary_difference'
                                    })
                   )
    return subordinates.sort_values(['hierarchy_level','subordinate_id'])

