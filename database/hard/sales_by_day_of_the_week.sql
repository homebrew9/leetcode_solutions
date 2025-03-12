-- Oracle
/* Write your PL/SQL query statement below */
with t (dow, category, quantity) as (
select to_char(o.order_date, 'fmDay') as dow, i.item_category as category, o.quantity
from items i
     left outer join orders o on (i.item_id = o.item_id)
)
select category,
       sum(case when dow='Monday' then quantity else 0 end) as "Monday",
       sum(case when dow='Tuesday' then quantity else 0 end) as "Tuesday",
       sum(case when dow='Wednesday' then quantity else 0 end) as "Wednesday",
       sum(case when dow='Thursday' then quantity else 0 end) as "Thursday",
       sum(case when dow='Friday' then quantity else 0 end) as "Friday",
       sum(case when dow='Saturday' then quantity else 0 end) as "Saturday",
       sum(case when dow='Sunday' then quantity else 0 end) as "Sunday"
from t
group by category
order by category
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (dow, category, quantity) as (
select to_char(o.order_date, 'fmDay') as dow, i.item_category as category, o.quantity
from items i
     left outer join orders o on (i.item_id = o.item_id)
)
select category,
       sum(case when dow='Monday' then quantity else 0 end) as "Monday",
       sum(case when dow='Tuesday' then quantity else 0 end) as "Tuesday",
       sum(case when dow='Wednesday' then quantity else 0 end) as "Wednesday",
       sum(case when dow='Thursday' then quantity else 0 end) as "Thursday",
       sum(case when dow='Friday' then quantity else 0 end) as "Friday",
       sum(case when dow='Saturday' then quantity else 0 end) as "Saturday",
       sum(case when dow='Sunday' then quantity else 0 end) as "Sunday"
from t
group by category
order by category
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (dow, category, quantity) as (
select datename(weekday, o.order_date) as dow, i.item_category as category, o.quantity
from items i
     left outer join orders o on (i.item_id = o.item_id)
)
select category,
       sum(case when dow='Monday' then quantity else 0 end) as "Monday",
       sum(case when dow='Tuesday' then quantity else 0 end) as "Tuesday",
       sum(case when dow='Wednesday' then quantity else 0 end) as "Wednesday",
       sum(case when dow='Thursday' then quantity else 0 end) as "Thursday",
       sum(case when dow='Friday' then quantity else 0 end) as "Friday",
       sum(case when dow='Saturday' then quantity else 0 end) as "Saturday",
       sum(case when dow='Sunday' then quantity else 0 end) as "Sunday"
from t
group by category
order by category
;


# MySQL
# Write your MySQL query statement below
with t (dow, category, quantity) as (
select dayname(o.order_date) as dow, i.item_category as category, o.quantity
from items i
     left outer join orders o on (i.item_id = o.item_id)
)
select category,
       sum(case when dow='Monday' then quantity else 0 end) as "Monday",
       sum(case when dow='Tuesday' then quantity else 0 end) as "Tuesday",
       sum(case when dow='Wednesday' then quantity else 0 end) as "Wednesday",
       sum(case when dow='Thursday' then quantity else 0 end) as "Thursday",
       sum(case when dow='Friday' then quantity else 0 end) as "Friday",
       sum(case when dow='Saturday' then quantity else 0 end) as "Saturday",
       sum(case when dow='Sunday' then quantity else 0 end) as "Sunday"
from t
group by category
order by category
;


# Pandas
import pandas as pd

def sales_by_day(orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df = items.merge(orders, how='left', on='item_id').rename(columns={'item_category': 'category'})
    all_weekdays = pd.CategoricalDtype(
        categories = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], 
        ordered=True)
    df['dayofweek'] = df['order_date'].dt.day_name().str.upper().astype(all_weekdays)
    df = df.pivot_table(index='category', columns='dayofweek', values='quantity', aggfunc='sum').reset_index()
    return df

