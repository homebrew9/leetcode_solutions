-- Oracle
/* Write your PL/SQL query statement below */
select round(x.total_items / y.total_orders, 2) as average_items_per_order
from (select sum(item_count * order_occurrences) as total_items from orders) x
     cross join
     (select sum(order_occurrences) as total_orders from orders) y
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select round(sum(item_count * order_occurrences)::numeric / sum(order_occurrences), 2) as average_items_per_order
  from orders
;


-- SQL Server
/* Write your T-SQL query statement below */
select round(x.total_items / y.total_orders, 2) as average_items_per_order
from (select convert(float, sum(item_count * order_occurrences)) as total_items from orders) x
     cross join
     (select convert(float, sum(order_occurrences)) as total_orders from orders) y
;


# MySQL
# Write your MySQL query statement below
select round(x.total_items / y.total_orders, 2) as average_items_per_order
from (select sum(item_count * order_occurrences) as total_items from orders) x
     cross join
     (select sum(order_occurrences) as total_orders from orders) y
;


# Pandas
import pandas as pd

def compressed_mean(orders: pd.DataFrame) -> pd.DataFrame:
    total_items = ( orders
                   .assign(items=orders['item_count']*orders['order_occurrences'])[['items']]
                   .sum()
                   .iloc[0]
                  )
    total_orders = ( orders[['order_occurrences']]
                    .sum()
                    .iloc[0]
                   )
    return pd.DataFrame(data={'average_items_per_order': round(total_items/total_orders, 2)}, index=[0])

