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


-- SQL Server


# MySQL


# Pandas

