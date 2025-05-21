-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, category) as (
    select pp.user_id, pi.category
      from ProductPurchases pp
           inner join ProductInfo pi on (pi.product_id = pp.product_id)
)
select t1.category as category1,
       t2.category as category2,
       count(distinct t1.user_id) as customer_count
  from t t1
       inner join t t2 on (t2.user_id = t1.user_id and t1.category < t2.category)
 group by t1.category, t2.category
having count(distinct t1.user_id) >= 3
order by customer_count desc, category1, category2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, category) as (
    select pp.user_id, pi.category
      from ProductPurchases pp
           inner join ProductInfo pi on (pi.product_id = pp.product_id)
)
select t1.category as category1,
       t2.category as category2,
       count(distinct t1.user_id) as customer_count
  from t t1
       inner join t t2 on (t2.user_id = t1.user_id and t1.category < t2.category)
 group by t1.category, t2.category
having count(distinct t1.user_id) >= 3
order by customer_count desc, category1, category2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, category) as (
    select pp.user_id, pi.category
      from ProductPurchases pp
           inner join ProductInfo pi on (pi.product_id = pp.product_id)
)
select t1.category as category1,
       t2.category as category2,
       count(distinct t1.user_id) as customer_count
  from t t1
       inner join t t2 on (t2.user_id = t1.user_id and t1.category < t2.category)
 group by t1.category, t2.category
having count(distinct t1.user_id) >= 3
order by customer_count desc, category1, category2
;


# MySQL
# Write your MySQL query statement below
with t (user_id, category) as (
    select pp.user_id, pi.category
      from ProductPurchases pp
           inner join ProductInfo pi on (pi.product_id = pp.product_id)
)
select t1.category as category1,
       t2.category as category2,
       count(distinct t1.user_id) as customer_count
  from t t1
       inner join t t2 on (t2.user_id = t1.user_id and t1.category < t2.category)
 group by t1.category, t2.category
having count(distinct t1.user_id) >= 3
order by customer_count desc, category1, category2
;








# Pandas

