-- Oracle
/* Write your PL/SQL query statement below */
with t (ad_id, total_clicked_and_viewed, total_clicked) as (
select ad_id,
       sum(case when action in ('Clicked','Viewed') then 1 else 0 end) as total_clicked_and_viewed,
       sum(case when action = 'Clicked' then 1 else 0 end) as total_clicked
from ads
group by ad_id
)
select ad_id,
       round(case when total_clicked_and_viewed = 0 then 0
                  else total_clicked / total_clicked_and_viewed
             end*100, 2) as ctr
from t
order by ctr desc, ad_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (ad_id, total_clicked_and_viewed, total_clicked) as (
select ad_id,
       sum(case when action in ('Clicked','Viewed') then 1 else 0 end)::float as total_clicked_and_viewed,
       sum(case when action = 'Clicked' then 1 else 0 end)::float as total_clicked
from ads
group by ad_id
)
select ad_id,
       round(case when total_clicked_and_viewed = 0 then 0
                  else total_clicked / total_clicked_and_viewed
             end::numeric*100, 2) as ctr
from t
order by ctr desc, ad_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (ad_id, total_clicked_and_viewed, total_clicked) as (
select ad_id,
       sum(case when action in ('Clicked','Viewed') then 1 else 0 end) as total_clicked_and_viewed,
       sum(case when action = 'Clicked' then 1 else 0 end) as total_clicked
from ads
group by ad_id
)
select ad_id,
       round(case when total_clicked_and_viewed = 0 then 0
                  else convert(float, total_clicked) / convert(float, total_clicked_and_viewed)
             end*100, 2) as ctr
from t
order by ctr desc, ad_id
;


# MySQL
# Write your MySQL query statement below
with t (ad_id, total_clicked_and_viewed, total_clicked) as (
select ad_id,
       sum(case when action in ('Clicked','Viewed') then 1 else 0 end) as total_clicked_and_viewed,
       sum(case when action = 'Clicked' then 1 else 0 end) as total_clicked
from ads
group by ad_id
)
select ad_id,
       round(case when total_clicked_and_viewed = 0 then 0
                  else total_clicked / total_clicked_and_viewed
             end*100, 2) as ctr
from t
order by ctr desc, ad_id
;


# Pandas
import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    df1 = (  ads[ads['action']=='Clicked']
             .groupby('ad_id',as_index=False)['action']
             .count()
             .rename(columns={'action':'clicked'})
          )
    df2 = (  ads[ads['action']!='Ignored']
             .groupby('ad_id',as_index=False)['action']
             .count()
             .rename(columns={'action':'total'})
          )
    df = pd.merge(df1, df2, how='inner', on='ad_id')
    df['ctr'] = round(df['clicked']/df['total']*100, 2)
    df = df[['ad_id', 'ctr']]
    return (  ads[['ad_id']]
              .drop_duplicates()
              .merge(df, how='left')
              .fillna(0.00)
              .sort_values(by=['ctr','ad_id'],ascending=[False,True])
           )

