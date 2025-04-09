-- Oracle
/* Write your PL/SQL query statement below */
with t (id, p_id, lvl, children) as (
    select id, p_id, 1, NULL
      from tree
     where p_id is null
    union all
    select t1.id, t.id, t.lvl + 1,
           (select count(*) from tree t2 where t2.p_id = t1.id)
      from tree t1
           inner join t on (t.id = t1.p_id)
)
select id,
       case when p_id is null then 'Root'
            when children = 0 then 'Leaf'
            else 'Inner'
       end as type
  from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select t.id,
       case when t.p_id is null then 'Root'
            when (select count(*) from tree t1 where t1.p_id = t.id) = 0 then 'Leaf'
            else 'Inner'
       end as type
  from tree t
;


-- SQL Server
/* Write your T-SQL query statement below */
select t.id,
       case when t.p_id is null then 'Root'
            when (select count(*) from tree t1 where t1.p_id = t.id) = 0 then 'Leaf'
            else 'Inner'
       end as type
  from tree t
;


# MySQL
# Write your MySQL query statement below
select t.id,
       case when t.p_id is null then 'Root'
            when (select count(*) from tree t1 where t1.p_id = t.id) = 0 then 'Leaf'
            else 'Inner'
       end as type
  from tree t
;


# Pandas
import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    root = tree[tree['p_id'].isna()]['id']
    parent = tree[~tree['p_id'].isna()][['p_id']].drop_duplicates()['p_id']
    return pd.concat(
                     [
                        tree[tree['id'].isin(root)][['id']].assign(type='Root'),
                        tree[(tree['id'].isin(parent)) & (~tree['id'].isin(root))][['id']].assign(type='Inner'),
                        tree[(~tree['id'].isin(parent)) & (~tree['id'].isin(root))][['id']].assign(type='Leaf')
                     ]
                    )

