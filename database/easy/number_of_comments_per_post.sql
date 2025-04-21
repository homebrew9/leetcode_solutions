-- Oracle
/* Write your PL/SQL query statement below */
with t (post_id) as (
    select distinct sub_id
      from submissions
     where parent_id is null
),
t1 (post_id, number_of_comments) as (
    select parent_id, count(distinct sub_id)
      from submissions
     where parent_id is not null
     group by parent_id
)
select t.post_id,
       coalesce(t1.number_of_comments, 0) as number_of_comments
  from t
       left outer join t1 on (t1.post_id = t.post_id)
 order by t.post_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (post_id) as (
    select distinct sub_id
      from submissions
     where parent_id is null
),
t1 (post_id, number_of_comments) as (
    select parent_id, count(distinct sub_id)
      from submissions
     where parent_id is not null
     group by parent_id
)
select t.post_id,
       coalesce(t1.number_of_comments, 0) as number_of_comments
  from t
       left outer join t1 on (t1.post_id = t.post_id)
 order by t.post_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (post_id) as (
    select distinct sub_id
      from submissions
     where parent_id is null
),
t1 (post_id, number_of_comments) as (
    select parent_id, count(distinct sub_id)
      from submissions
     where parent_id is not null
     group by parent_id
)
select t.post_id,
       coalesce(t1.number_of_comments, 0) as number_of_comments
  from t
       left outer join t1 on (t1.post_id = t.post_id)
 order by t.post_id
;


# MySQL
# Write your MySQL query statement below
with t (post_id) as (
    select distinct sub_id
      from submissions
     where parent_id is null
),
t1 (post_id, number_of_comments) as (
    select parent_id, count(distinct sub_id)
      from submissions
     where parent_id is not null
     group by parent_id
)
select t.post_id,
       coalesce(t1.number_of_comments, 0) as number_of_comments
  from t
       left outer join t1 on (t1.post_id = t.post_id)
 order by t.post_id
;


# Pandas
import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    posts = (submissions[submissions['parent_id'].isna()][['sub_id']]
             .drop_duplicates()
             .rename(columns={'sub_id':'post_id'})
            )
    comments = (submissions[~submissions['parent_id'].isna()]
                .drop_duplicates()
                .groupby('parent_id',as_index=False)['sub_id']
                .count()
                .rename(columns={'parent_id':'post_id','sub_id':'number_of_comments'})
               )
    return posts.merge(comments, how='left', on='post_id').fillna(0).sort_values(by='post_id')

