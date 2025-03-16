-- Oracle
/* Write your PL/SQL query statement below */
with t_hier (employee_id, employee_name, manager_id, lvl, root_node, path, salary) as (
    select employee_id, employee_name, manager_id, 1, employee_id, to_char(employee_id), salary
      from employees
	 --where manager_id is null
    union all
    select e.employee_id, e.employee_name, e.manager_id, th.lvl + 1, th.root_node,
           th.path || ',' || e.employee_id, e.salary
      from employees e
           inner join t_hier th on (e.manager_id = th.employee_id)
)
select th.employee_id, th.employee_name, th.lvl as "level",
       count(*) - 1 as team_size,
       sum(th1.salary) as budget
  from t_hier th
       inner join t_hier th1 on (th1.root_node = th.employee_id)
 where th.root_node = (select th2.root_node from t_hier th2 where th2.manager_id is null)
 group by th.employee_id, th.employee_name, th.lvl
 order by th.lvl, budget desc, th.employee_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t_hier (employee_id, employee_name, manager_id, level, root_node, path, salary) as (
    select employee_id, employee_name, manager_id, 1, employee_id, employee_id::text, salary
      from employees
	 --where manager_id is null
    union all
    select e.employee_id, e.employee_name, e.manager_id, th.level + 1, th.root_node,
           th.path::text || ',' || e.employee_id::text, e.salary
      from employees e
           inner join t_hier th on (e.manager_id = th.employee_id)
)
select th.employee_id, th.employee_name, th.level,
       count(*) - 1 as team_size,
       sum(th1.salary) as budget
  from t_hier th
       inner join t_hier th1 on (th1.root_node = th.employee_id)
 where th.root_node = (select th2.root_node from t_hier th2 where th2.manager_id is null)
 group by th.employee_id, th.employee_name, th.level
 order by th.level, budget desc, th.employee_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_hier (employee_id, employee_name, manager_id, level, root_node, path, salary) as (
    select employee_id, employee_name, manager_id, 1, employee_id, convert(varchar(max), employee_id), salary
      from employees
	 --where manager_id is null
    union all
    select e.employee_id, e.employee_name, e.manager_id, th.level + 1, th.root_node,
           convert(varchar(max), th.path) + ',' + convert(varchar(max), e.employee_id), e.salary
      from employees e
           inner join t_hier th on (e.manager_id = th.employee_id)
)
select th.employee_id, th.employee_name, th.level,
       count(*) - 1 as team_size,
       sum(th1.salary) as budget
  from t_hier th
       inner join t_hier th1 on (th1.root_node = th.employee_id)
 where th.root_node = (select th2.root_node from t_hier th2 where th2.manager_id is null)
 group by th.employee_id, th.employee_name, th.level
 order by th.level, budget desc, th.employee_name
;


# MySQL
# Write your MySQL query statement below
with recursive t_hier (employee_id, employee_name, manager_id, level, root_node, path, salary) as (
    select employee_id, employee_name, manager_id, 1, employee_id, employee_id, salary
      from employees
    union all
    select e.employee_id, e.employee_name, e.manager_id, th.level + 1, th.root_node,
           th.path || ',' || e.employee_id, e.salary
      from employees e
           inner join t_hier th on (e.manager_id = th.employee_id)
)
select th.employee_id, th.employee_name, th.level,
       count(*) - 1 as team_size,
       sum(th1.salary) as budget
  from t_hier th
       inner join t_hier th1 on (th1.root_node = th.employee_id)
 where th.root_node = (select th2.root_node from t_hier th2 where th2.manager_id is null)
 group by th.employee_id, th.employee_name, th.level
 order by th.level, budget desc, th.employee_name
;


# Pandas
import pandas as pd

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    global res
    res = None
    def get_teamsize_budget(p_employee_id):
        df = employees[employees['employee_id'] == p_employee_id]
        team_size, budget = 0, 0
        while len(df) > 0:
            team_size += len(df)
            budget += df['salary'].sum()
            df1 = ( df
                   .merge(employees, how='inner', left_on='employee_id', right_on='manager_id')[['employee_id_y','salary_y']]
                   .rename(columns={'employee_id_y':'employee_id', 'salary_y':'salary'})
                  )
            df = df1
        return (team_size-1, budget)
    def get_hierarchy(p_employee_id):
        global res
        res = None
        level = 0
        df = employees[employees['employee_id'] == p_employee_id][['employee_id','employee_name']]
        while len(df) > 0:
            level += 1
            df['level'] = level
            res = df if res is None else pd.concat([res, df])
            df1 = ( df
                   .merge(employees, how='inner', left_on='employee_id', right_on='manager_id')[['employee_id_y','employee_name_y']]
                   .rename(columns={'employee_id_y': 'employee_id', 'employee_name_y': 'employee_name'})
                  )
            df = df1
    employees[employees['manager_id'].isna()]['employee_id'].apply(get_hierarchy)
    res['team_size'] = res['employee_id'].apply(get_teamsize_budget).str[0]
    res['budget'] = res['employee_id'].apply(get_teamsize_budget).str[1]
    return res.sort_values(by=['level','budget','employee_name'], ascending=[True,False,True])

