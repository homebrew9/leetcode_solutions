-- Oracle
/* Write your PL/SQL query statement below */
select activity
from friends
group by activity
having count(*) != (select x.cnt
                    from (select count(*) as cnt from friends group by activity order by cnt
                         ) x
                    where rownum=1
                   )
and count(*) != (select x.cnt
                 from (select count(*) as cnt from friends group by activity order by cnt desc
                      ) x
                 where rownum=1
                )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select activity
from friends
group by activity
having count(*) != (select count(*) from friends group by activity order by count(*) limit 1)
and count(*) != (select count(*) from friends group by activity order by count(*) desc limit 1)
;


-- SQL Server
/* Write your T-SQL query statement below */
select activity
from friends
group by activity
having count(*) != (select top 1 count(*) from friends group by activity order by count(*))
and count(*) != (select top 1 count(*) from friends group by activity order by count(*) desc)
;


# MySQL
# Write your MySQL query statement below
select activity
from friends
group by activity
having count(*) != (select count(*) from friends group by activity order by count(*) limit 1)
and count(*) != (select count(*) from friends group by activity order by count(*) desc limit 1)
;


# Pandas
import pandas as pd

def activity_participants(friends: pd.DataFrame, activities: pd.DataFrame) -> pd.DataFrame:
    df = friends.groupby('activity',as_index=False)['id'].count()
    min_max = df.agg({'id': ['min','max']})
    return df[~df['id'].isin(min_max['id'])][['activity']]

