-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select customer_id,
        sum(case when (to_char(order_timestamp, 'HH24:MI:SS') between '11:00:00' and '14:00:00') or
                      (to_char(order_timestamp, 'HH24:MI:SS') between '18:00:00' and '21:00:00')
                    then 1
                    else 0
            end) as peak_hour_orders,
        count(order_id) as total_orders,
        avg(order_rating) as avg_rating,
        sum(case when order_rating is not null then 1 else 0 end) as rated_orders
    from restaurant_orders
    group by customer_id
)
select customer_id,
       total_orders,
       round(peak_hour_orders / total_orders * 100) as peak_hour_percentage,
       round(avg_rating, 2) as average_rating
  from t
 where total_orders >= 3
   and peak_hour_orders/total_orders >= 0.6
   and avg_rating >= 4
   and rated_orders/total_orders >= 0.5
 order by avg_rating desc, customer_id desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select customer_id,
           sum(case when (to_char(order_timestamp, 'HH24:MI:SS') between '11:00:00' and '14:00:00') or
                         (to_char(order_timestamp, 'HH24:MI:SS') between '18:00:00' and '21:00:00')
                    then 1
                    else 0
               end) as peak_hour_orders,
           count(order_id) as total_orders,
           avg(order_rating) as avg_rating,
           sum(case when order_rating is not null then 1 else 0 end) as rated_orders
      from restaurant_orders
     group by customer_id
)
select customer_id,
       total_orders,
       round(peak_hour_orders::numeric / total_orders * 100) as peak_hour_percentage,
       round(avg_rating, 2) as average_rating
  from t
 where total_orders >= 3
   and peak_hour_orders::numeric/total_orders >= 0.6
   and avg_rating >= 4
   and rated_orders::numeric/total_orders >= 0.5
 order by avg_rating desc, customer_id desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select customer_id,
           sum(case when (RIGHT(CONVERT(VARCHAR, order_timestamp, 120), 8) between '11:00:00' and '14:00:00') or
                         (RIGHT(CONVERT(VARCHAR, order_timestamp, 120), 8) between '18:00:00' and '21:00:00')
                    then 1
                    else 0
               end) as peak_hour_orders,
           count(order_id) as total_orders,
           avg(CONVERT(NUMERIC, order_rating)) as avg_rating,
           sum(case when order_rating is not null then 1 else 0 end) as rated_orders
      from restaurant_orders
     group by customer_id
)
select customer_id,
       total_orders,
       round(CONVERT(NUMERIC, peak_hour_orders) / total_orders * 100, 0) as peak_hour_percentage,
       round(avg_rating, 2) as average_rating
  from t
 where total_orders >= 3
   and CONVERT(NUMERIC, peak_hour_orders)/total_orders >= 0.6
   and avg_rating >= 4
   and CONVERT(NUMERIC, rated_orders)/total_orders >= 0.5
 order by avg_rating desc, customer_id desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select customer_id,
           sum(case when (DATE_FORMAT(order_timestamp, '%H:%M:%S') between '11:00:00' and '14:00:00') or
                         (DATE_FORMAT(order_timestamp, '%H:%M:%S') between '18:00:00' and '21:00:00')
                    then 1
                    else 0
               end) as peak_hour_orders,
           count(order_id) as total_orders,
           avg(order_rating) as avg_rating,
           sum(case when order_rating is not null then 1 else 0 end) as rated_orders
      from restaurant_orders
     group by customer_id
)
select customer_id,
       total_orders,
       round(peak_hour_orders / total_orders * 100) as peak_hour_percentage,
       round(avg_rating, 2) as average_rating
  from t
 where total_orders >= 3
   and peak_hour_orders/total_orders >= 0.6
   and avg_rating >= 4
   and rated_orders/total_orders >= 0.5
 order by avg_rating desc, customer_id desc
;


# Pandas
import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    restaurant_orders.order_timestamp = pd.to_datetime(restaurant_orders.order_timestamp)
    restaurant_orders['is_peak_hour'] = np.where(
       ( ('11:00:00' <= restaurant_orders['order_timestamp'].dt.strftime('%H:%M:%S')) &
         (restaurant_orders['order_timestamp'].dt.strftime('%H:%M:%S') <= '14:00:00')
       ) |
       ( ('18:00:00' <= restaurant_orders['order_timestamp'].dt.strftime('%H:%M:%S')) &
         (restaurant_orders['order_timestamp'].dt.strftime('%H:%M:%S') <= '21:00:00')
       ),
       1, 0
    )
    df = ( restaurant_orders
          .groupby('customer_id', as_index=0)
          .agg(rated_orders=('order_rating','count'),
               peak_hour_orders=('is_peak_hour','sum'),
               total_orders=('order_id','count'),
               average_rating=('order_rating','mean')
           )
         )
    df['peak_hour_percentage'] = df['peak_hour_orders']/df['total_orders']*100
    df['rated_order_pct'] = df['rated_orders'] / df['total_orders']
    df1 = ( df
           .query('total_orders >= 3 and \
                   peak_hour_percentage >= 60 and \
                   average_rating >= 4 and \
                   rated_order_pct >= 0.5'
                 )[['customer_id','total_orders','peak_hour_percentage','average_rating']]
          )
    df1['peak_hour_percentage'] = round(df1['peak_hour_percentage'])
    df1['average_rating'] = round(df1['average_rating'], 2)
    df2 = df1.sort_values(by=['average_rating','customer_id'], ascending=[False,False])
    return df2












