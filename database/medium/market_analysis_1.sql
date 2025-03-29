-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select order_id, order_date, buyer_id
    from orders
    where to_char(order_date, 'YYYY') = '2019'
)
select u.user_id as "buyer_id",
       to_char(u.join_date, 'YYYY-MM-DD') as "join_date",
       sum(decode(t.order_id,null,0,1)) as "orders_in_2019"
from users u
     left outer join t on (t.buyer_id = u.user_id)
group by u.user_id, to_char(u.join_date, 'YYYY-MM-DD')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select u.user_id as buyer_id, u.join_date, coalesce(count(o.order_id), 0) as orders_in_2019
  from users u
       left outer join orders o on (o.buyer_id = u.user_id and to_char(o.order_date, 'yyyy') = '2019')
  group by u.user_id, u.join_date
 order by u.user_id
;


-- SQL Server


# MySQL
# Write your MySQL query statement below
select u.user_id as buyer_id,
       u.join_date,
       coalesce(count(o.order_id), 0) as orders_in_2019
from users u
     left outer join orders o on (o.buyer_id = u.user_id and date_format(o.order_date, '%Y') = '2019')
group by u.user_id, u.join_date
;


# Pandas

