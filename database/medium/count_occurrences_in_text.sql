-- Oracle
/* Write your PL/SQL query statement below */
select 'bull' as word, (select count(*) from files where regexp_like(content, '\sbull\s')) as count from dual
union all
select 'bear' as word, (select count(*) from files where regexp_like(content, '\sbear\s')) as count from dual
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select 'bull' as word, (select count(*) from files where regexp_like(content, '\sbull\s')) as count
union all
select 'bear' as word, (select count(*) from files where regexp_like(content, '\sbear\s')) as count
;


-- SQL Server
/* Write your T-SQL query statement below */
select 'bull' as word, (select count(*) from files where content like '% bull %') as count
union all
select 'bear' as word, (select count(*) from files where content like '% bear %') as count
;


# MySQL
# Write your MySQL query statement below
select 'bull' as word, (select count(*) from files where content LIKE '% bull %') as count
union all
select 'bear' as word, (select count(*) from files where content LIKE '% bear %') as count
;


# Pandas
import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull_count = len(files[files['content'].str.contains('^.* bull .*$')])
    bear_count = len(files[files['content'].str.contains('^.* bear .*$')])
    return pd.DataFrame(data={'word': ['bull','bear'], 'count': [bull_count, bear_count]})

