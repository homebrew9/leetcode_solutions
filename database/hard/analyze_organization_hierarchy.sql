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

