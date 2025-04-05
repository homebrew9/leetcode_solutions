-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select contact_id, type, duration, floor(duration/3600) as hours,
           duration - floor(duration/3600) * 3600 as seconds_in_the_last_hour
      from calls
),
t1 as (
    select contact_id, type, duration, hours,
           floor(seconds_in_the_last_hour/60) as minutes,
           seconds_in_the_last_hour - floor(seconds_in_the_last_hour/60) * 60 as seconds
      from t
),
t2 as (
select co.first_name, t1.type, t1.duration,
       lpad(to_char(hours),2,'0') || ':' ||
       lpad(to_char(minutes),2,'0') || ':' ||
       lpad(to_char(seconds),2,'0') as duration_formatted,
       dense_rank() over (partition by t1.type order by t1.duration desc, co.first_name desc) as drnk
  from contacts co
       inner join t1 on (t1.contact_id = co.id)
)
select first_name, type, duration_formatted
from t2
where drnk <= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select contact_id, type, duration, to_char((duration||' second')::interval, 'HH24:MI:SS') as duration_formatted
      from calls
),
t1 as (
select co.first_name, t.type, t.duration, t.duration_formatted,
       dense_rank() over (partition by t.type order by t.duration desc, co.first_name desc) as drnk
  from contacts co
       inner join t on (t.contact_id = co.id)
)
select first_name, type, duration_formatted
from t1
where drnk <= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (contact_id, type, duration, duration_formatted) as (
    select contact_id, type, duration, --CONVERT(TIME(0), DATEADD(SS, duration, 0), 108)
           RIGHT('00'+CONVERT(VARCHAR(10),duration/3600),2)  +':' +
           RIGHT('00'+CONVERT(VARCHAR(2),(duration%3600)/60),2) +':' +
           RIGHT('00'+CONVERT(VARCHAR(2),duration%60),2)
      from calls
),
t1 as (
    select co.first_name, t.type, t.duration, t.duration_formatted,
           dense_rank() over (partition by t.type order by t.duration desc, co.first_name desc) as drnk
      from contacts co
           inner join t on (t.contact_id = co.id)
)
select first_name, type, duration_formatted
  from t1
 where drnk <= 3
;


# MySQL
# Write your MySQL query statement below
with t (contact_id, type, duration, duration_formatted) as (
    select contact_id, type, duration, date_format(timestamp(sec_to_time(duration)), '%H:%i:%s')
      from calls
)
,
t1 as (
select co.first_name, t.type, t.duration, t.duration_formatted,
       dense_rank() over (partition by t.type order by t.duration desc, co.first_name desc) as drnk
  from contacts co
       inner join t on (t.contact_id = co.id)
)
select first_name, type, duration_formatted
from t1
where drnk <= 3
;


# Pandas
import pandas as pd

def find_longest_calls(contacts: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    calls['duration_formatted'] = pd.to_datetime(calls['duration'], unit='s').dt.strftime('%H:%M:%S')
    df = ( contacts
          .merge(calls, how='inner', left_on='id', right_on='contact_id')
          .sort_values(by=['type','duration','first_name'], ascending=[True,False,True])
         )
    return ( df
            .assign(rnk = df.groupby('type', as_index=0)['duration'].rank(method='dense', ascending=False))
            .query('rnk <= 3')[['first_name','type','duration_formatted']]
           )

