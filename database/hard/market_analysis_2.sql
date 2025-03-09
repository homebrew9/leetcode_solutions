-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select u.user_id as seller_id, o.order_date, o.item_id, i.item_brand, u.favorite_brand,
       dense_rank() over (partition by u.user_id order by order_date) as drnk,
       count(*) over (partition by u.user_id) as cnt
from users u
     inner join orders o on (o.seller_id = u.user_id)
     inner join items i on (i.item_id = o.item_id)
)
select seller_id,
       case
           when drnk = 1 and cnt = 1 then 'no'
           when drnk = 2 and item_brand = favorite_brand then 'yes'
           else 'no'
       end as "2nd_item_fav_brand"
from t
where ((cnt = 1 and drnk = 1) or drnk = 2)
union all
select user_id, 'no'
from users
where user_id not in (select seller_id from orders)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select u.user_id as seller_id, o.order_date, o.item_id, i.item_brand, u.favorite_brand,
       dense_rank() over (partition by u.user_id order by order_date) as drnk,
       count(*) over (partition by u.user_id) as cnt
from users u
     inner join orders o on (o.seller_id = u.user_id)
     inner join items i on (i.item_id = o.item_id)
)
select seller_id,
       case
           when drnk = 1 and cnt = 1 then 'no'
           when drnk = 2 and item_brand = favorite_brand then 'yes'
           else 'no'
       end as "2nd_item_fav_brand"
from t
where ((cnt = 1 and drnk = 1) or drnk = 2)
union all
select user_id, 'no'
from users
where user_id not in (select seller_id from orders)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select u.user_id as seller_id, o.order_date, o.item_id, i.item_brand, u.favorite_brand,
       dense_rank() over (partition by u.user_id order by order_date) as drnk,
       count(*) over (partition by u.user_id) as cnt
from users u
     inner join orders o on (o.seller_id = u.user_id)
     inner join items i on (i.item_id = o.item_id)
)
select seller_id,
       case
           when drnk = 1 and cnt = 1 then 'no'
           when drnk = 2 and item_brand = favorite_brand then 'yes'
           else 'no'
       end as "2nd_item_fav_brand"
from t
where ((cnt = 1 and drnk = 1) or drnk = 2)
union all
select user_id, 'no'
from users
where user_id not in (select seller_id from orders)
;


# MySQL
# Write your MySQL query statement below
with t as (
select u.user_id as seller_id, o.order_date, o.item_id, i.item_brand, u.favorite_brand,
       dense_rank() over (partition by u.user_id order by order_date) as drnk,
       count(*) over (partition by u.user_id) as cnt
from users u
     inner join orders o on (o.seller_id = u.user_id)
     inner join items i on (i.item_id = o.item_id)
)
select seller_id,
       case
           when drnk = 1 and cnt = 1 then 'no'
           when drnk = 2 and item_brand = favorite_brand then 'yes'
           else 'no'
       end as "2nd_item_fav_brand"
from t
where ((cnt = 1 and drnk = 1) or drnk = 2)
union all
select user_id, 'no'
from users
where user_id not in (select seller_id from orders)
;


# Pandas
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = ( orders
          .assign(rnk= orders
                      .groupby('seller_id',as_index=False)['order_date']
                      .rank(method='dense')
                 )
          .query('rnk==2')
          .merge(items,how='inner',on='item_id')
         )
    df1 = ( users
           .merge( df,
                   how='left',
                   left_on=['user_id','favorite_brand'],
                   right_on=['seller_id','item_brand']
                 )[['user_id','item_brand']]
          )
    df1['item_brand'] = np.where(df1['item_brand'].isna(),'no','yes')
    df1 = df1.rename(columns={'user_id':'seller_id','item_brand':'2nd_item_fav_brand'})
    return df1

