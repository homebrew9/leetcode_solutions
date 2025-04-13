-- Oracle
/* Write your PL/SQL query statement below */
select distinct c.title
  from TVProgram t
       inner join Content c on (c.content_id = t.content_id and c.kids_content = 'Y' and content_type = 'Movies')
 where to_char(t.program_date, 'YYYY-MM') = '2020-06'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct c.title
  from TVProgram t
       inner join Content c on (c.content_id = t.content_id and c.kids_content = 'Y' and content_type = 'Movies')
 where to_char(t.program_date, 'YYYY-MM') = '2020-06'
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct c.title
from tvprogram t
     inner join content c on (c.content_id = t.content_id)
where year(t.program_date) = 2020
and month(t.program_date) = 6
and c.kids_content = 'Y'
and c.content_type = 'Movies'
;


# MySQL
# Write your MySQL query statement below
select distinct c.title
from tvprogram t
     inner join content c on (c.content_id = t.content_id)
where year(t.program_date) = 2020
and month(t.program_date) = 6
and c.kids_content = 'Y'
and c.content_type = 'Movies'
;


# Pandas
import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    df1 = ( tv_program[(tv_program['program_date'] >= '2020-06-01 00:00') & \
                       (tv_program['program_date'] <= '2020-06-30 23:59')][['content_id']]
          )
    df2 = ( content[(content['Kids_content']=='Y') & \
                    (content['content_type']=='Movies')][['content_id','title']]
          )
    return df1.merge(df2, how='inner', on='content_id')[['title']].drop_duplicates()

