-- Oracle
/* Write your PL/SQL query statement below */
select round(sum(x.tiv_2016), 2) as tiv_2016
  from Insurance x
 where exists (select null from Insurance y where y.pid != x.pid and y.tiv_2015 = x.tiv_2015)
   and not exists (select null from Insurance z where z.pid != x.pid and z.lat = x.lat and z.lon = x.lon)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select round(sum(x.tiv_2016)::numeric, 2) as tiv_2016
  from Insurance x
 where exists (select null from Insurance y where y.pid != x.pid and y.tiv_2015 = x.tiv_2015)
   and not exists (select null from Insurance z where z.pid != x.pid and z.lat = x.lat and z.lon = x.lon)
;


-- SQL Server
/* Write your T-SQL query statement below */
select round(convert(float, sum(x.tiv_2016)), 2) as tiv_2016
  from Insurance x
 where exists (select null from Insurance y where y.pid != x.pid and y.tiv_2015 = x.tiv_2015)
   and not exists (select null from Insurance z where z.pid != x.pid and z.lat = x.lat and z.lon = x.lon)
;


# MySQL
# Write your MySQL query statement below
select round(sum(x.tiv_2016), 2) as tiv_2016
  from Insurance x
 where exists (select null from Insurance y where y.pid != x.pid and y.tiv_2015 = x.tiv_2015)
   and not exists (select null from Insurance z where z.pid != x.pid and z.lat = x.lat and z.lon = x.lon)
;


# Pandas
import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    df = ( insurance
          .merge(insurance, on='tiv_2015')
          .query('pid_x != pid_y')[['pid_x','lat_x','lon_x','tiv_2016_x']]
          .drop_duplicates()
          .rename(columns={'pid_x':'pid','lat_x':'lat','lon_x':'lon','tiv_2016_x':'tiv_2016'})
         )
    invalid_pid_list = ( df
                        .merge(insurance, how='inner', left_on=['lat','lon'], right_on=['lat','lon'])
                        .query('pid_x != pid_y')[['pid_x']]
                        .drop_duplicates()
                        .rename(columns={'pid_x':'pid'})
                       )
    tiv_2016_sum = round(df[~df['pid'].isin(invalid_pid_list['pid'])]['tiv_2016'].sum(), 2)
    return pd.DataFrame(data={'tiv_2016': [tiv_2016_sum]})
