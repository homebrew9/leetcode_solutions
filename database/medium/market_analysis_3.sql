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
-- Version 1 - Using DENSE_RANK analytic function
with t (seller_id, num_items) as (
    select o.seller_id, count(distinct o.item_id) as num_items
      from orders o
           inner join items i on (i.item_id = o.item_id)
     where not exists (select null
                         from users u
                        where u.seller_id = o.seller_id
                          and u.favorite_brand = i.item_brand
                      )
     group by o.seller_id
),
t1 as (
    select seller_id, num_items,
           dense_rank() over (order by num_items desc) as drnk
      from t
)
select seller_id, num_items
  from t1
 where drnk = 1
 order by seller_id
;

-- Version 2 - Using MAX and avoiding the DENSE_RANK analytic function
with t (seller_id, num_items) as (
    select o.seller_id, count(distinct o.item_id) as num_items
      from orders o
           inner join items i on (i.item_id = o.item_id)
     where not exists (select null
                         from users u
                        where u.seller_id = o.seller_id
                          and u.favorite_brand = i.item_brand
                      )
     group by o.seller_id
)
select seller_id, num_items
  from t
 where num_items = (select max(num_items) from t)
 order by seller_id
;

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

