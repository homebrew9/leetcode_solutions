-- Oracle
/* Write your PL/SQL query statement below */
with t (article_id, author_id, viewer_id, view_date) as (
    select distinct article_id, author_id, viewer_id, view_date
      from views
)
select distinct viewer_id as id
from t
group by viewer_id, view_date
having count(*) > 1
order by viewer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (article_id, author_id, viewer_id, view_date) as (
    select distinct article_id, author_id, viewer_id, view_date
      from views
)
select distinct viewer_id as id
from t
group by viewer_id, view_date
having count(*) > 1
order by viewer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (article_id, author_id, viewer_id, view_date) as (
    select distinct article_id, author_id, viewer_id, view_date
      from views
)
select distinct viewer_id as id
from t
group by viewer_id, view_date
having count(*) > 1
order by viewer_id
;


# MySQL
# Write your MySQL query statement below
with t (article_id, author_id, viewer_id, view_date) as (
    select distinct article_id, author_id, viewer_id, view_date
      from views
)
select distinct viewer_id as id
from t
group by viewer_id, view_date
having count(*) > 1
order by viewer_id
;


# Pandas
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.drop_duplicates().rename(columns={'viewer_id': 'id'})
    return ( views
            .groupby(['id','view_date'],as_index=False)['article_id']
            .count()
            .query('article_id > 1')[['id']]
            .drop_duplicates()
            .sort_values('id')
           )

