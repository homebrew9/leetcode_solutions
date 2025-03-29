-- Oracle


-- PostgreSQL


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

