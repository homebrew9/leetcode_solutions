-- Oracle
/* Write your PL/SQL query statement below */
with s (subtask_id) as (
    select level as subtask_id
      from dual
   connect by level <= (select max(subtasks_count) from tasks)
),
p (task_id, subtasks_count, subtask_id) as (
    select t.task_id, t.subtasks_count, s.subtask_id
      from tasks t
           cross join s
)
select p.task_id, p.subtask_id
  from p
 where p.subtask_id <= p.subtasks_count
minus
select e.task_id, e.subtask_id
  from executed e
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (task_id, subtasks_count, subtask_id) as (
    select task_id, subtasks_count, 1 as subtask_id
    from tasks
    union all
    select x.task_id, x.subtasks_count, t.subtask_id + 1
    from tasks x
         inner join t on (t.task_id = x.task_id and t.subtask_id + 1 <= t.subtasks_count)
)
select t.task_id, t.subtask_id
from t
     left outer join executed e on (e.task_id = t.task_id and e.subtask_id = t.subtask_id)
where e.subtask_id is null
order by task_id, subtask_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (task_id, subtasks_count, subtask_id) as (
    select task_id, subtasks_count, 1 as subtask_id
    from tasks
    union all
    select x.task_id, x.subtasks_count, t.subtask_id + 1
    from tasks x
         inner join t on (t.task_id = x.task_id and t.subtask_id + 1 <= t.subtasks_count)
)
select t.task_id, t.subtask_id
from t
     left outer join executed e on (e.task_id = t.task_id and e.subtask_id = t.subtask_id)
where e.subtask_id is null
order by task_id, subtask_id
;


# MySQL
# Write your MySQL query statement below
with recursive t (task_id, subtasks_count, subtask_id) as (
    select task_id, subtasks_count, 1 as subtask_id
    from tasks
    union all
    select x.task_id, x.subtasks_count, t.subtask_id + 1
    from tasks x
         inner join t on (t.task_id = x.task_id and t.subtask_id + 1 <= t.subtasks_count)
)
select t.task_id, t.subtask_id
from t
     left outer join executed e on (e.task_id = t.task_id and e.subtask_id = t.subtask_id)
where e.subtask_id is null
order by task_id, subtask_id
;


# Pandas
import pandas as pd

def find_subtasks(tasks: pd.DataFrame, executed: pd.DataFrame) -> pd.DataFrame:
    max_val = tasks['subtasks_count'].max()
    df = pd.Series(range(1, max_val+1)).to_frame().rename(columns={0:'subtask_id'})
    df = tasks.merge(df, how='cross').query('subtask_id <= subtasks_count')
    executed['status'] = 1
    return ( df
            .merge(executed, how='left', on=['task_id','subtask_id'])
            .fillna(0)
            .query('status == 0')[['task_id','subtask_id']]
           )

