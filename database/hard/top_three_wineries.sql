-- Oracle
/* Write your PL/SQL query statement below */
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then winery||' ('||total_points||')' else null end) as top_winery,
       nvl(max(case when drnk = 2 then winery||' ('||total_points||')' else null end), 'No second winery') as second_winery,
       nvl(max(case when drnk = 3 then winery||' ('||total_points||')' else null end), 'No third winery') as third_winery
from t1
group by country
order by country
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (country, winery, total_points) as (
    select country, winery, sum(points) as total_points
      from wineries
     group by country, winery
),
t1 as (
select country, winery, total_points,
       row_number() over (partition by country order by total_points desc, winery) as rnum
from t
)
select country,
       max(case when rnum=1 then winery||' ('||total_points::text||')' end) as top_winery,
       coalesce(max(case when rnum=2 then winery||' ('||total_points::text||')' end), 'No second winery') as second_winery,
       coalesce(max(case when rnum=3 then winery||' ('||total_points::text||')' end), 'No third winery') as third_winery
from t1
group by country
order by country
;


-- SQL Server
/* Write your T-SQL query statement below */
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then winery+' ('+convert(varchar,total_points)+')' else null end) as top_winery,
       isnull(
           max(case when drnk = 2 then winery+' ('+convert(varchar,total_points)+')' else null end),
           'No second winery'
       ) as second_winery,
       isnull(
           max(case when drnk = 3 then winery+' ('+convert(varchar,total_points)+')' else null end),
           'No third winery'
       ) as third_winery
from t1
group by country
order by country
;


# MySQL
# Write your MySQL query statement below
--
with t (country, winery, total_points) as (
select country, winery, sum(points) as total_points
from wineries
group by country, winery
),
t1 (country, winery, total_points, drnk) as (
select country, winery, total_points,
       dense_rank() over (partition by country order by total_points desc, winery) as drnk
from t
)
select country,
       max(case when drnk = 1 then concat(winery,' (',total_points,')') else null end) as top_winery,
       coalesce(
           max(case when drnk = 2 then concat(winery,' (',total_points,')') else null end),
           'No second winery'
       ) as second_winery,
       coalesce(
           max(case when drnk = 3 then concat(winery,' (',total_points,')') else null end),
           'No third winery'
       ) as third_winery
from t1
group by country
order by country
;


# Pandas
import pandas as pd

def top_three_wineries(wineries: pd.DataFrame) -> pd.DataFrame:
    df_ranks = pd.DataFrame(data={'rnum':[1,2,3], 'values':['No top winery','No second winery','No third winery']})
    df_cntry_ranks = df_ranks.merge(wineries[['country']].drop_duplicates(), how='cross')
    df = ( wineries
        .groupby(['country','winery'],as_index=0)['points']
        .sum()
        .sort_values(['country','points','winery'],ascending=[True,False,True])
        )
    df['rnum'] = df.groupby(['country']).cumcount()+1
    df['wp'] = df['winery'] + ' (' + df['points'].astype('str') + ')'
    df1 = df_cntry_ranks.merge(df, how='left', on=['country','rnum'])
    df1['wp'] = np.where(df1['wp'].isna(), df1['values'], df1['wp'])
    df1 = ( df1
        .pivot_table(index='country', columns='rnum', values='wp', aggfunc='max')
        .reset_index()[['country',1,2,3]]
        .rename(columns={1:'top_winery', 2:'second_winery', 3:'third_winery'})
        )
    return df1

