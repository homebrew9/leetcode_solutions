-- Oracle
/* Write your PL/SQL query statement below */
with t_hier(node, parent, type) as (
    select t.n, t.p, 'Root'
      from tree t
     where t.p is null
    union all
    select t1.n, t1.p,
           case when (select count(*) from tree where p = t1.n) = 0
                then 'Leaf'
                else 'Inner'
           end
      from tree t1
           inner join t_hier t on (t.node = t1.p)
)
select node as n, type
from t_hier
order by node
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t_hier(node, parent, type) as (
    select t.n, t.p, 'Root'
      from tree t
     where t.p is null
    union all
    select t1.n, t1.p,
           case when (select count(*) from tree where p = t1.n) = 0
                then 'Leaf'
                else 'Inner'
           end
      from tree t1
           inner join t_hier t on (t.node = t1.p)
)
select node as n, type
from t_hier
order by node
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_hier(node, parent, [type]) as (
    select t.n, t.p, convert(varchar(10), 'Root')
      from tree t
     where t.p is null
    union all
    select t1.n, t1.p,
           convert(varchar(10), 'Inner')
      from tree t1
           inner join t_hier t on (t.node = t1.p)
     where exists (select null from tree x where x.p = t1.n)
    union all
    select t1.n, t1.p,
           convert(varchar(10), 'Leaf')
      from tree t1
           inner join t_hier t on (t.node = t1.p)
     where not exists (select null from tree x where x.p = t1.n)
)
select node as n, [type]
from t_hier
order by node
;


# MySQL
# Write your MySQL query statement below
with recursive t_hier(node, parent, type) as (
    select t.n, t.p, cast('Root' as char(10))
      from tree t
     where t.p is null
    union all
    select t1.n, t1.p,
           cast( case when (select count(*) from tree where p = t1.n) = 0
                      then 'Leaf'
                      else 'Inner'
                 end
                 as char(10)
               )
      from tree t1
           inner join t_hier t on (t.node = t1.p)
)
select node as n, type
from t_hier
order by node
;


# Pandas
import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
    root = tree[tree['P'].isna()]['N']
    parent = tree[~tree['P'].isna()][['P']].drop_duplicates()['P']
    return pd.concat(
                     [
                        tree[tree['N'].isin(root)][['N']].assign(Type='Root'),
                        tree[(tree['N'].isin(parent)) & (~tree['N'].isin(root))][['N']].assign(Type='Inner'),
                        tree[(~tree['N'].isin(parent)) & (~tree['N'].isin(root))][['N']].assign(Type='Leaf')
                     ]
                    ).sort_values('N')

