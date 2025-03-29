-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select order_id, order_date, buyer_id
    from orders
    where to_char(order_date, 'YYYY') = '2019'
)
select u.user_id as "buyer_id",
       to_char(u.join_date, 'YYYY-MM-DD') as "join_date",
       sum(decode(t.order_id,null,0,1)) as "orders_in_2019"
from users u
     left outer join t on (t.buyer_id = u.user_id)
group by u.user_id, to_char(u.join_date, 'YYYY-MM-DD')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select u.user_id as buyer_id, u.join_date, coalesce(count(o.order_id), 0) as orders_in_2019
  from users u
       left outer join orders o on (o.buyer_id = u.user_id and to_char(o.order_date, 'yyyy') = '2019')
  group by u.user_id, u.join_date
 order by u.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select u.user_id as buyer_id, u.join_date, coalesce(count(o.order_id), 0) as orders_in_2019
  from users u
       left outer join orders o on (o.buyer_id = u.user_id and year(o.order_date) = 2019)
  group by u.user_id, u.join_date
 order by u.user_id
;


# MySQL
# Write your MySQL query statement below
select u.user_id as buyer_id,
       u.join_date,
       coalesce(count(o.order_id), 0) as orders_in_2019
from users u
     left outer join orders o on (o.buyer_id = u.user_id and date_format(o.order_date, '%Y') = '2019')
group by u.user_id, u.join_date
;


# Pandas
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = ( orders[orders['order_date'].dt.strftime('%Y') == '2019']
          .groupby('buyer_id', as_index=0)['order_id'].count()
         )
    return ( users
            .merge(df, how='left', left_on='user_id', right_on='buyer_id')
            .fillna(0)[['user_id','join_date','order_id']]
            .rename(columns={'user_id': 'buyer_id', 'order_id': 'orders_in_2019'})
           )

