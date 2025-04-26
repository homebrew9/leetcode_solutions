-- Oracle
/* Write your PL/SQL query statement below */
select distinct author_id as "id"
from views
where author_id = viewer_id
order by author_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct author_id as id
  from views
 where author_id = viewer_id
 order by id
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct author_id as id
  from views
 where author_id = viewer_id
 order by id
;


# MySQL
# Write your MySQL query statement below
select distinct author_id as id
from views
where author_id = viewer_id
order by id
;


# Pandas
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views['author_id']==views['viewer_id']][
               ['author_id']
           ].drop_duplicates().rename(
               columns={'author_id':'id'}
           ).sort_values(['id'])

