-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select item_type, count(*) as total_count, sum(square_footage) as total_footage
      from inventory
     group by item_type
)
select t.item_type,
       case when t.item_type = 'prime_eligible'
            then floor(500000 / t.total_footage) * t.total_count
            when t.item_type = 'not_prime'
            then floor((500000 - floor(500000 / v.total_footage) * v.total_footage) / t.total_footage) * t.total_count
       end as item_count
from t
     cross join (select total_footage from t where item_type = 'prime_eligible') v
order by item_count desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select item_type, count(*) as total_count, sum(square_footage) as total_footage
      from inventory
     group by item_type
)
select t.item_type,
       case when t.item_type = 'prime_eligible'
            then floor(500000 / t.total_footage) * t.total_count
            when t.item_type = 'not_prime'
            then floor((500000 - floor(500000 / v.total_footage) * v.total_footage) / t.total_footage) * t.total_count
       end as item_count
from t
     cross join (select total_footage from t where item_type = 'prime_eligible') v
order by item_count desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select item_type, count(*) as total_count, sum(square_footage) as total_footage
      from inventory
     group by item_type
)
select t.item_type,
       case when t.item_type = 'prime_eligible'
            then floor(500000 / t.total_footage) * t.total_count
            when t.item_type = 'not_prime'
            then floor((500000 - floor(500000 / v.total_footage) * v.total_footage) / t.total_footage) * t.total_count
       end as item_count
from t
     cross join (select total_footage from t where item_type = 'prime_eligible') v
order by item_count desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select item_type, count(*) as total_count, sum(square_footage) as total_footage
      from inventory
     group by item_type
)
select t.item_type,
       case when t.item_type = 'prime_eligible'
            then floor(500000 / t.total_footage) * t.total_count
            when t.item_type = 'not_prime'
            then floor((500000 - floor(500000 / v.total_footage) * v.total_footage) / t.total_footage) * t.total_count
       end as item_count
from t
     cross join (select total_footage from t where item_type = 'prime_eligible') v
order by item_count desc
;


# Pandas
import pandas as pd

def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:
    df_prime = ( inventory[inventory['item_type'] == 'prime_eligible']
                .groupby('item_type',as_index=0)['square_footage']
                .agg(['count', 'sum'])
               )
    df_notprime = ( inventory[inventory['item_type'] == 'not_prime']
                   .groupby('item_type',as_index=0)['square_footage']
                   .agg(['count', 'sum'])
                  )
    df_prime['combinations'] = (500000 / df_prime['sum']).astype(int)
    df_prime['total_footage'] = df_prime['combinations'] * df_prime['sum']
    df_prime['item_count'] = df_prime['count'] * df_prime['combinations']
    df_notprime['combinations'] = ((500000 - df_prime['total_footage']).astype(int) / df_notprime['sum']).astype(int)
    df_notprime['item_count'] = df_notprime['count'] * df_notprime['combinations']
    return ( pd.concat(
                        [df_prime[['item_type','item_count']],
                         df_notprime[['item_type','item_count']]
                        ]
                      ).sort_values(by='item_count', ascending=False)
           )

