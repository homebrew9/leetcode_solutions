-- Oracle
/* Write your PL/SQL query statement below */
with t (event_type, avg_activity) as (
select event_type, avg(occurrences) as avg_activity
from events
group by event_type
)
select e.business_id
from events e
     inner join t on (t.event_type = e.event_type and e.occurrences > t.avg_activity)
group by e.business_id
having count(*) > 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (event_type, avg_activity) as (
select event_type, avg(occurrences) as avg_activity
from events
group by event_type
)
select e.business_id
from events e
     inner join t on (t.event_type = e.event_type and e.occurrences > t.avg_activity)
group by e.business_id
having count(*) > 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select business_id
  from events 
       join (select event_type, avg(occurrences) occur
               from events
              group by event_type
            ) b
       on (events.event_type = b.event_type and occurrences > occur)
 group by business_id
having count(distinct events.event_type) > 1
;


# MySQL
# Write your MySQL query statement below
with t (event_type, avg_activity) as (
select event_type, avg(occurrences) as avg_activity
from events
group by event_type
)
select e.business_id
from events e
     inner join t on (t.event_type = e.event_type and e.occurrences > t.avg_activity)
group by e.business_id
having count(*) > 1
;


# Pandas
import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    df = (  events
           .groupby('event_type',as_index=False)['occurrences']
           .mean()
           .rename(columns={'occurrences':'avg_activity'})
         )
    return (  events
             .merge(df, how='inner', on='event_type')
             .query('occurrences > avg_activity')
             .groupby('business_id',as_index=False)['event_type']
             .count()
             .query('event_type > 1')[['business_id']]
           )

