-- Oracle
/* Write your PL/SQL query statement below */
with t (product_id, purchase_date, units, total_price) as (
select us.product_id, us.purchase_date, us.units, us.units * p.price as total_price
from unitssold us
     inner join prices p on (p.product_id = us.product_id and us.purchase_date between p.start_date and p.end_date)
)
select product_id, round(sum(total_price)/sum(units), 2) as average_price
from t
group by product_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select u.product_id, round(sum(u.units * p.price)::numeric / sum(u.units), 2) as average_price
  from UnitsSold u
       inner join Prices p on (p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date)
 group by u.product_id
union all
select distinct p1.product_id, 0 as average_price
  from prices p1
 where not exists (select null from UnitsSold u1 where u1.product_id = p1.product_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select u.product_id, round(convert(float, sum(u.units * p.price)) / sum(u.units), 2) as average_price
  from UnitsSold u
       inner join Prices p on (p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date)
 group by u.product_id
union all
select distinct p1.product_id, 0 as average_price
  from prices p1
 where not exists (select null from UnitsSold u1 where u1.product_id = p1.product_id)
;


# MySQL
# Write your MySQL query statement below
select u.product_id, round(sum(u.units * p.price) / sum(u.units), 2) as average_price
  from UnitsSold u
       inner join Prices p on (p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date)
 group by u.product_id
union all
select distinct p1.product_id, 0 as average_price
  from prices p1
 where not exists (select null from UnitsSold u1 where u1.product_id = p1.product_id)
;


# Pandas
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = units_sold.merge(prices, how='inner', on='product_id').query('start_date <= purchase_date <= end_date')
    df['total_price'] = df['units'] * df['price']
    df = df.groupby('product_id', as_index=0).agg({'total_price': 'sum', 'units': 'sum'})
    df['average_price'] = round(df['total_price'] / df['units'], 2)
    df = df[['product_id', 'average_price']]
    df1 = prices[~prices['product_id'].isin(units_sold['product_id'])][['product_id']].drop_duplicates()
    df1['average_price'] = 0
    return pd.concat([df, df1])

