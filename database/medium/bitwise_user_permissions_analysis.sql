-- Oracle
/* Write your PL/SQL query statement below */
-- BITOR(x, y) = x + y - BITAND(x, y)
-- Oracle has BITAND() function but not BITOR()
with t1 (user_id, permissions, rnum, cnt) as (
    select user_id, permissions,
           row_number() over (order by user_id) as rnum,
           count(*) over () as cnt
      from user_permissions
),
t_hier (user_id, permissions, rnum, cnt, ba_perm, bo_perm) as (
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt, t1.permissions, t1.permissions
      from t1
     where t1.rnum = 1
    union all
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt,
           bitand(t_hier.ba_perm, t1.permissions),
           t_hier.bo_perm + t1.permissions - bitand(t_hier.bo_perm, t1.permissions)
      from t1
           inner join t_hier on (t1.rnum = t_hier.rnum + 1)
)
select ba_perm as common_perms, bo_perm as any_perms
from t_hier
where rnum = cnt
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Bitwise AND operator: &
-- Bitwise OR operator: |
with recursive t1 (user_id, permissions, rnum, cnt) as (
    select user_id, permissions,
           row_number() over (order by user_id) as rnum,
           count(*) over () as cnt
      from user_permissions
),
t_hier (user_id, permissions, rnum, cnt, ba_perm, bo_perm) as (
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt, t1.permissions, t1.permissions
      from t1
     where t1.rnum = 1
    union all
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt,
           t_hier.ba_perm & t1.permissions,
           t_hier.bo_perm | t1.permissions
      from t1
           inner join t_hier on (t1.rnum = t_hier.rnum + 1)
)
select ba_perm as common_perms, bo_perm as any_perms
from t_hier
where rnum = cnt
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Bitwise AND operator: &
-- Bitwise OR operator: |
with t1 (user_id, permissions, rnum, cnt) as (
    select user_id, permissions,
           row_number() over (order by user_id) as rnum,
           count(*) over () as cnt
      from user_permissions
),
t_hier (user_id, permissions, rnum, cnt, ba_perm, bo_perm) as (
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt, t1.permissions, t1.permissions
      from t1
     where t1.rnum = 1
    union all
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt,
           t_hier.ba_perm & t1.permissions,
           t_hier.bo_perm | t1.permissions
      from t1
           inner join t_hier on (t1.rnum = t_hier.rnum + 1)
)
select ba_perm as common_perms, bo_perm as any_perms
from t_hier
where rnum = cnt
;


# MySQL
# Write your MySQL query statement below
-- Bitwise AND operator: &
-- Bitwise OR operator: |
with recursive t1 (user_id, permissions, rnum, cnt) as (
    select user_id, permissions,
           row_number() over (order by user_id) as rnum,
           count(*) over () as cnt
      from user_permissions
),
t_hier (user_id, permissions, rnum, cnt, ba_perm, bo_perm) as (
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt, t1.permissions, t1.permissions
      from t1
     where t1.rnum = 1
    union all
    select t1.user_id, t1.permissions, t1.rnum, t1.cnt,
           t_hier.ba_perm & t1.permissions,
           t_hier.bo_perm | t1.permissions
      from t1
           inner join t_hier on (t1.rnum = t_hier.rnum + 1)
)
select ba_perm as common_perms, bo_perm as any_perms
from t_hier
where rnum = cnt
;


# Pandas
import pandas as pd
from functools import reduce

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    # Functional way of calculating AND and OR
    common_perms = reduce(lambda x,y: x&y, user_permissions.permissions)
    any_perms = reduce(lambda x,y: x|y, user_permissions.permissions)
    return pd.DataFrame(data={'common_perms': [common_perms], 'any_perms': [any_perms]})

