-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select id, visit_date, people,
           id - row_number() over (order by id) as group_id
      from stadium
     where people >= 100
),
t1 as (
select id, visit_date, people, group_id,
       count(*) over (partition by group_id) as cnt
  from t
)
select id, to_char(visit_date, 'yyyy-mm-dd') as visit_date, people
  from t1
 where cnt >= 3
 order by visit_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, visit_date, people,
           id - row_number() over (order by id) as group_id
      from stadium
     where people >= 100
),
t1 as (
select id, visit_date, people, group_id,
       count(*) over (partition by group_id) as cnt
  from t
)
select id, to_char(visit_date, 'yyyy-mm-dd') as visit_date, people
  from t1
 where cnt >= 3
 order by visit_date
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select id, visit_date, people,
           id - row_number() over (order by id) as group_id
      from stadium
     where people >= 100
),
t1 as (
select id, visit_date, people, group_id,
       count(*) over (partition by group_id) as cnt
  from t
)
select id, visit_date, people
  from t1
 where cnt >= 3
 order by visit_date
;


# MySQL
# Write your MySQL query statement below
with t as (
    select id, visit_date, people,
           id - row_number() over (order by id) as group_id
      from stadium
     where people >= 100
),
t1 as (
select id, visit_date, people, group_id,
       count(*) over (partition by group_id) as cnt
  from t
)
select id, visit_date, people
  from t1
 where cnt >= 3
 order by visit_date
;


# Pandas
import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    df = stadium[stadium['people']>=100]
    df = df.assign(rn=range(1,len(df)+1))
    df['group_id'] = df['id'] - df['rn']
    df['cnt'] = df.groupby('group_id')['id'].transform('count')
    return ( df
            .query('people>=100 and cnt>=3')[['id','visit_date','people']]
            .sort_values('visit_date')
           )

