-- Oracle
/* Write your PL/SQL query statement below */
with t (product_id, new_price, change_date, max_change_date) as (
    select product_id, new_price, change_date,
           max(change_date) over (partition by product_id) as max_change_date
      from products
     where trunc(change_date) <= DATE'2019-08-16'
),
t1 (product_id, price) as (
    select product_id, new_price as price
      from t
     where change_date = max_change_date
),
t2 (product_id, price) as (
    select distinct product_id, 10 as price
      from products
     where product_id not in (select product_id from t1)
)
select t1.product_id, t1.price from t1
union all
select t2.product_id, t2.price from t2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (product_id, price) as (
    select p1.product_id, p1.new_price as price
      from products p1
     where p1.change_date = (
                                select max(p2.change_date)
                                  from products p2
                                 where p2.product_id = p1.product_id
                                   and p2.change_date <= '2019-08-16'::date
                            )
)
select distinct p.product_id, coalesce(t.price, 10) as price
  from products p
       left outer join t on (t.product_id = p.product_id)
;


-- SQL Server


# MySQL


# Pandas

