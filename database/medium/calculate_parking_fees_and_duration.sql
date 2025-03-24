-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select car_id, lot_id, (exit_time - entry_time) * 24 as hours, fee_paid
      from parkingtransactions
),
t1 as (
    select car_id, lot_id, sum(hours) as time_in_lot
      from t
     group by car_id, lot_id
),
t2 as (
    select x.car_id, x.lot_id
      from (
              select car_id, lot_id, time_in_lot,
                     dense_rank() over (partition by car_id order by time_in_lot desc) as drnk
                from t1
           ) x
     where x.drnk = 1
)
select t.car_id,
       sum(t.fee_paid) as total_fee_paid,
       round(sum(t.fee_paid) / sum(t.hours), 2) as avg_hourly_fee,
       t2.lot_id as most_time_lot
from t
     inner join t2 on (t2.car_id = t.car_id)
group by t.car_id, t2.lot_id
order by t.car_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select car_id, lot_id,
           extract(epoch from (exit_time - entry_time))::numeric / 60 / 60  as hours,
           fee_paid
      from parkingtransactions
),
t1 as (
    select car_id, lot_id, sum(hours) as time_in_lot
      from t
     group by car_id, lot_id
),
t2 as (
    select x.car_id, x.lot_id
      from (
              select car_id, lot_id, time_in_lot,
                     dense_rank() over (partition by car_id order by time_in_lot desc) as drnk
                from t1
           ) x
     where x.drnk = 1
)
select t.car_id,
       sum(t.fee_paid) as total_fee_paid,
       round(sum(t.fee_paid)::numeric / sum(t.hours), 2) as avg_hourly_fee,
       t2.lot_id as most_time_lot
from t
     inner join t2 on (t2.car_id = t.car_id)
group by t.car_id, t2.lot_id
order by t.car_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select car_id, lot_id,
           convert(float, datediff(second, entry_time, exit_time)) / 60 / 60 as hours,
           fee_paid
      from parkingtransactions
),
t1 as (
    select car_id, lot_id, sum(hours) as time_in_lot
      from t
     group by car_id, lot_id
),
t2 as (
    select x.car_id, x.lot_id
      from (
              select car_id, lot_id, time_in_lot,
                     dense_rank() over (partition by car_id order by time_in_lot desc) as drnk
                from t1
           ) x
     where x.drnk = 1
)
select t.car_id,
       sum(t.fee_paid) as total_fee_paid,
       round(convert(float, sum(t.fee_paid)) / sum(t.hours), 2) as avg_hourly_fee,
       t2.lot_id as most_time_lot
from t
     inner join t2 on (t2.car_id = t.car_id)
group by t.car_id, t2.lot_id
order by t.car_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select car_id, lot_id,
           timestampdiff(second, entry_time, exit_time) / 60 / 60 as hours,
           fee_paid
      from parkingtransactions
),
t1 as (
    select car_id, lot_id, sum(hours) as time_in_lot
      from t
     group by car_id, lot_id
),
t2 as (
    select x.car_id, x.lot_id
      from (
              select car_id, lot_id, time_in_lot,
                     dense_rank() over (partition by car_id order by time_in_lot desc) as drnk
                from t1
           ) x
     where x.drnk = 1
)
select t.car_id,
       sum(t.fee_paid) as total_fee_paid,
       round(sum(t.fee_paid) / sum(t.hours), 2) as avg_hourly_fee,
       t2.lot_id as most_time_lot
from t
     inner join t2 on (t2.car_id = t.car_id)
group by t.car_id, t2.lot_id
order by t.car_id
;


# Pandas
import pandas as pd

def calculate_fees_and_duration(parking_transactions: pd.DataFrame) -> pd.DataFrame:
    parking_transactions['hours'] = ( (parking_transactions['exit_time']
                                       - parking_transactions['entry_time']
                                      ).dt.seconds/60/60
                                    )
    df = ( parking_transactions
          .groupby(['car_id','lot_id'],as_index=0)['hours']
          .sum()
          .sort_values(by=['car_id','hours'],ascending=[True,False])
         )
    df_most_time_lot = ( df
                        .assign(
                                 drnk= df.groupby('car_id',as_index=0)['hours']
                                         .rank(method='dense', ascending=False)
                               )
                        .query('drnk == 1')[['car_id','lot_id']]
                       )
    df_most_time_lot.rename(columns={'lot_id': 'most_time_lot'}, inplace=True)
    df_fees = ( parking_transactions
               .groupby('car_id',as_index=0)
               .agg({'fee_paid':'sum', 'hours':'sum'})
              )
    df_fees['avg_hourly_fee'] = round(df_fees['fee_paid'] / df_fees['hours'], 2)
    df_fees.rename(columns={'fee_paid': 'total_fee_paid'},inplace=True)
    return ( df_fees
            .merge(df_most_time_lot, how='inner', on='car_id')[[
                'car_id',
                'total_fee_paid',
                'avg_hourly_fee',
                'most_time_lot'
            ]]
            .sort_values(['car_id'])
           )

