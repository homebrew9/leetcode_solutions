-- Oracle
/* Write your PL/SQL query statement below */
with month_runner (month_no) as (
    select 1 as month_no from dual
    union all
    select mr.month_no + 1 from month_runner mr where mr.month_no + 1 <= 12
),
statistics_year (month_no, month) as (
select month_no, add_months(DATE'2020-01-01', month_no-1) as month
from month_runner
),
t as (
select trunc(join_date, 'MM') as month,
       count(*) over (order by trunc(join_date, 'MM')) as active_drivers
from drivers
),
t1 as (
select trunc(r.requested_at, 'MM') as month,
       count(*) as accepted_rides
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by trunc(r.requested_at, 'MM')
)
select distinct sy.month_no as month,
       coalesce(t.active_drivers, lag(t.active_drivers ignore nulls) over (order by sy.month_no), 0) as active_drivers,
       coalesce(t1.accepted_rides, 0) as accepted_rides
from statistics_year sy
     left outer join t on (t.month = sy.month)
     left outer join t1 on (t1.month = sy.month)
order by sy.month_no
;


# Pandas
import pandas as pd

def hopper_company(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    all_months = pd.DataFrame(data={'month': range(1,13)})
    all_months = all_months.assign(mth=pd.to_datetime('2020-'+all_months['month'].astype(str).str.zfill(2)+'-01'),
                                   mth_fmt='2020-'+all_months['month'].astype(str).str.zfill(2)
                                  )
    drivers['join_month'] = drivers['join_date'].dt.strftime('%Y-%m')
    df = ( all_months
          .merge(drivers, how='cross')
          .query('join_month <= mth_fmt')
          .groupby(['month','mth'], as_index=False)['driver_id']
          .count()
          .rename(columns={'driver_id':'active_drivers'})
         )
    df = all_months.merge(df, how='left', on=['month','mth']).fillna(0)
    rides['requested_month'] = pd.to_datetime(rides['requested_at'].dt.strftime('%Y-%m-01'))
    df1 = ( rides
           .merge(accepted_rides, how='inner', on='ride_id')
           .groupby('requested_month',as_index=False)['ride_id']
           .count()
           .rename(columns={'ride_id':'accepted_rides'})
          )
    return ( df
            .merge(df1, how='left', left_on='mth', right_on='requested_month')
            .fillna(0)[['month','active_drivers','accepted_rides']]
            .sort_values('month')
           )

