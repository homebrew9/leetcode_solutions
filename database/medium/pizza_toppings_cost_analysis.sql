-- Oracle
/* Write your PL/SQL query statement below */
select distinct t1.topping_name||','||t2.topping_name||','||t3.topping_name as pizza,
       round(t1.cost+t2.cost+t3.cost, 2) as total_cost
from toppings t1
     inner join toppings t2 on t1.topping_name < t2.topping_name
     inner join toppings t3 on t2.topping_name < t3.topping_name
order by total_cost desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct t1.topping_name||','||t2.topping_name||','||t3.topping_name as pizza,
       round(t1.cost+t2.cost+t3.cost, 2) as total_cost
from toppings t1
     inner join toppings t2 on t1.topping_name < t2.topping_name
     inner join toppings t3 on t2.topping_name < t3.topping_name
order by total_cost desc
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct t1.topping_name + ',' + t2.topping_name + ',' + t3.topping_name as pizza,
       round(t1.cost + t2.cost + t3.cost, 2) as total_cost
from toppings t1
     inner join toppings t2 on t1.topping_name < t2.topping_name
     inner join toppings t3 on t2.topping_name < t3.topping_name
order by total_cost desc
;


# MySQL
# Write your MySQL query statement below
select distinct concat(t1.topping_name, ',', t2.topping_name, ',', t3.topping_name) as pizza,
       round(t1.cost + t2.cost + t3.cost, 2) as total_cost
from toppings t1
     inner join toppings t2 on t1.topping_name < t2.topping_name
     inner join toppings t3 on t2.topping_name < t3.topping_name
order by total_cost desc, pizza
;


# Pandas
import pandas as pd

def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
    df = (toppings
          .merge(toppings, how='cross').query('topping_name_x < topping_name_y')
          .merge(toppings, how='cross').query('topping_name_y < topping_name')
         )
    df['pizza'] = df['topping_name_x']+','+df['topping_name_y']+','+df['topping_name']
    df['total_cost'] = round(df['cost_x'] + df['cost_y'] + df['cost'], 2)
    return df[['pizza','total_cost']].sort_values(by=['total_cost', 'pizza'], ascending=[False, True])

