-- Oracle
/* Write your PL/SQL query statement below */
with t (seller_id, item_id) as (
select u.seller_id, i.item_id
from users u
     inner join items i on (i.item_brand = u.favorite_brand)
),
t1 (seller_id, num_items) as (
select o.seller_id, count(distinct o.item_id) as num_items
from orders o
where not exists (select null
                    from t
                   where t.seller_id = o.seller_id
                     and t.item_id = o.item_id
                 )
group by o.seller_id
)
select x.seller_id, x.num_items
from t1 x
where x.num_items = (select max(num_items) from t1)
order by x.seller_id
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t (seller_id, item_id) as (
select u.seller_id, i.item_id
from users u
     inner join items i on (i.item_brand = u.favorite_brand)
),
t1 (seller_id, num_items) as (
select o.seller_id, count(distinct o.item_id) as num_items
from orders o
where not exists (select null
                    from t
                   where t.seller_id = o.seller_id
                     and t.item_id = o.item_id
                 )
group by o.seller_id
)
select x.seller_id, x.num_items
from t1 x
where x.num_items = (select max(num_items) from t1)
order by x.seller_id
;


# MySQL
# Write your MySQL query statement below
with t (seller_id, item_id) as (
select u.seller_id, i.item_id
from users u
     inner join items i on (i.item_brand = u.favorite_brand)
),
t1 (seller_id, num_items) as (
select o.seller_id, count(distinct o.item_id) as num_items
from orders o
where not exists (select null
                    from t
                   where t.seller_id = o.seller_id
                     and t.item_id = o.item_id
                 )
group by o.seller_id
)
select x.seller_id, x.num_items
from t1 x
where x.num_items = (select max(num_items) from t1)
order by x.seller_id
;


# Pandas
# There is no option for Pandas in the drop-down.

