-- Oracle
/* Write your PL/SQL query statement below */
with t (bin, min_duration, max_duration) as (
    select '[0-5>', 0, 299 from dual union all
    select '[5-10>', 300, 599 from dual union all
    select '[10-15>', 600, 899 from dual union all
    select '15 or more', 900, power(10,20) from dual
)
select t.bin, count(s.session_id) as total
from t
     left outer join sessions s on (s.duration between t.min_duration and t.max_duration)
group by t.bin
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (bin, min_duration, max_duration) as (
    select '[0-5>', 0, 299 union all
    select '[5-10>', 300, 599 union all
    select '[10-15>', 600, 899 union all
    select '15 or more', 900, power(10,20)
)
select t.bin, count(s.session_id) as total
from t
     left outer join sessions s on (s.duration between t.min_duration and t.max_duration)
group by t.bin
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (bin, min_duration, max_duration) as (
    select '[0-5>', 0, 299 union all
    select '[5-10>', 300, 599 union all
    select '[10-15>', 600, 899 union all
    select '15 or more', 900, power(10,6)
)
select t.bin, count(s.session_id) as total
from t
     left outer join sessions s on (s.duration between t.min_duration and t.max_duration)
group by t.bin
;


# MySQL
# Write your MySQL query statement below
with t (bin, min_duration, max_duration) as (
    select '[0-5>', 0, 299 union all
    select '[5-10>', 300, 599 union all
    select '[10-15>', 600, 899 union all
    select '15 or more', 900, power(10,20)
)
select t.bin, count(s.session_id) as total
from t
     left outer join sessions s on (s.duration between t.min_duration and t.max_duration)
group by t.bin
;


# Pandas
import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    sessions['bin'] = (  np.where(sessions['duration'] >= 900, '15 or more',
                             np.where(sessions['duration'] >= 600, '[10-15>',
                                 np.where(sessions['duration'] >= 300, '[5-10>',
                                    '[0-5>'
                                 )
                             )
                         )
                      )
    bin_data = {'bin': ['[0-5>','[5-10>','[10-15>','15 or more']}
    df = pd.DataFrame(data=bin_data)
    df1 = sessions.groupby('bin', as_index=False)['session_id'].count()
    return df.merge(df1, how='left', on='bin').fillna(0).rename(columns={'session_id':'total'})

