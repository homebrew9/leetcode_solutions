-- Oracle
/* Write your PL/SQL query statement below */
with t (store_id, n_products) as (
    select store_id, count(distinct product_name) as n_products
    from inventory
    group by store_id
    having count(distinct product_name) >= 3
),
t1 as (
    select i.store_id, i.price, i.quantity, i.product_name,
        dense_rank() over (partition by i.store_id order by i.price desc) as drnk_most_expensive,
        dense_rank() over (partition by i.store_id order by i.price) as drnk_cheapest
    from inventory i
        inner join t on (t.store_id = i.store_id)
)
select s.store_id, s.store_name, s.location,
       exp.product_name as most_exp_product,
       chp.product_name as cheapest_product,
       round(chp.quantity / exp.quantity, 2) as imbalance_ratio
  from (select store_id, product_name, quantity from t1 where drnk_most_expensive = 1) exp
       inner join
       (select store_id, product_name, quantity from t1 where drnk_cheapest = 1) chp
       on (chp.store_id = exp.store_id and chp.quantity > exp.quantity)
       inner join stores s on (s.store_id = exp.store_id)
 order by imbalance_ratio desc, store_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (store_id, n_products) as (
    select store_id, count(distinct product_name) as n_products
    from inventory
    group by store_id
    having count(distinct product_name) >= 3
),
t1 as (
    select i.store_id, i.price, i.quantity, i.product_name,
        dense_rank() over (partition by i.store_id order by i.price desc) as drnk_most_expensive,
        dense_rank() over (partition by i.store_id order by i.price) as drnk_cheapest
    from inventory i
        inner join t on (t.store_id = i.store_id)
)
select s.store_id, s.store_name, s.location,
       exp.product_name as most_exp_product,
       chp.product_name as cheapest_product,
       round(chp.quantity::numeric / exp.quantity, 2) as imbalance_ratio
  from (select store_id, product_name, quantity from t1 where drnk_most_expensive = 1) exp
       inner join
       (select store_id, product_name, quantity from t1 where drnk_cheapest = 1) chp
       on (chp.store_id = exp.store_id and chp.quantity > exp.quantity)
       inner join stores s on (s.store_id = exp.store_id)
 order by imbalance_ratio desc, store_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (store_id, n_products) as (
    select store_id, count(distinct product_name) as n_products
    from inventory
    group by store_id
    having count(distinct product_name) >= 3
),
t1 as (
    select i.store_id, i.price, i.quantity, i.product_name,
        dense_rank() over (partition by i.store_id order by i.price desc) as drnk_most_expensive,
        dense_rank() over (partition by i.store_id order by i.price) as drnk_cheapest
    from inventory i
        inner join t on (t.store_id = i.store_id)
)
select s.store_id, s.store_name, s.location,
       exp.product_name as most_exp_product,
       chp.product_name as cheapest_product,
       round(convert(float, chp.quantity) / exp.quantity, 2) as imbalance_ratio
  from (select store_id, product_name, quantity from t1 where drnk_most_expensive = 1) exp
       inner join
       (select store_id, product_name, quantity from t1 where drnk_cheapest = 1) chp
       on (chp.store_id = exp.store_id and chp.quantity > exp.quantity)
       inner join stores s on (s.store_id = exp.store_id)
 order by imbalance_ratio desc, store_name
;


# MySQL
# Write your MySQL query statement below
with t (store_id, n_products) as (
    select store_id, count(distinct product_name) as n_products
    from inventory
    group by store_id
    having count(distinct product_name) >= 3
),
t1 as (
    select i.store_id, i.price, i.quantity, i.product_name,
        dense_rank() over (partition by i.store_id order by i.price desc) as drnk_most_expensive,
        dense_rank() over (partition by i.store_id order by i.price) as drnk_cheapest
    from inventory i
        inner join t on (t.store_id = i.store_id)
)
select s.store_id, s.store_name, s.location,
       exp.product_name as most_exp_product,
       chp.product_name as cheapest_product,
       round(chp.quantity / exp.quantity, 2) as imbalance_ratio
  from (select store_id, product_name, quantity from t1 where drnk_most_expensive = 1) exp
       inner join
       (select store_id, product_name, quantity from t1 where drnk_cheapest = 1) chp
       on (chp.store_id = exp.store_id and chp.quantity > exp.quantity)
       inner join stores s on (s.store_id = exp.store_id)
 order by imbalance_ratio desc, store_name
;


# Pandas
import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    valid_store_ids = ( inventory
                       .groupby('store_id', as_index=0)
                       .agg(n_distinct_products=('product_name', 'nunique'))
                       .query('n_distinct_products >= 3')['store_id']
                      )
    df = ( inventory[inventory['store_id'].isin(valid_store_ids)]
          .sort_values(by=['store_id','price'])
         )
    df['drnk_cheapest'] = ( df
                           .groupby('store_id', as_index=0)['price']
                           .rank(method='dense')
                          )
    df['drnk_most_expensive'] = ( df
                                 .groupby('store_id', as_index=0)['price']
                                 .rank(method='dense', ascending=False)
                                )
    df_cheapest = df.query('drnk_cheapest == 1')[['store_id','product_name','quantity']]
    df_most_expensive = df.query('drnk_most_expensive == 1')[['store_id','product_name','quantity']]
    df1 = ( df_cheapest
           .merge(df_most_expensive, how='inner', on='store_id')
           .query('quantity_x > quantity_y')
           .merge(stores, how='inner', on='store_id')
           .rename(columns={'product_name_x': 'cheapest_product', 'product_name_y': 'most_exp_product'})
          )
    df1['imbalance_ratio'] = round(df1['quantity_x'] / df1['quantity_y'], 2)
    return ( df1[['store_id','store_name','location','most_exp_product','cheapest_product','imbalance_ratio']]
            .sort_values(by=['imbalance_ratio','store_name'], ascending=[False,True])
           )

