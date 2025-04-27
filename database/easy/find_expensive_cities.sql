-- Oracle
/* Write your PL/SQL query statement below */
select x.city
from listings x
group by x.city
having avg(x.price) > (select avg(y.price) from listings y)
order by x.city
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select listing_id, city, price,
       avg(price) over (partition by city) as city_avg,
       avg(price) over () as national_avg
  from listings
)
select distinct city
  from t
 where city_avg > national_avg
 order by city
;


-- SQL Server
/* Write your T-SQL query statement below */
select x.city
from listings x
group by x.city
having avg(x.price) > (select avg(y.price) from listings y)
order by x.city
;


# MySQL
# Write your MySQL query statement below
select x.city
from listings x
group by x.city
having avg(x.price) > (select avg(y.price) from listings y)
order by x.city
;


# Pandas
import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    national_avg = listings[['price']].mean()[0]
    df = listings.groupby('city', as_index=0)['price'].mean()
    return df[df['price'] > national_avg][['city']].sort_values('city')

