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
import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    df = product_purchases.merge(product_info, how='inner', on='product_id')[['user_id', 'category']]
    return ( df
            .merge(df, how='inner', on='user_id')
            .query('category_x < category_y')
            .groupby(['category_x','category_y'], as_index=0)['user_id']
            .nunique()
            .query('user_id >= 3')
            .rename(columns={'category_x':'category1', 'category_y':'category2', 'user_id':'customer_count'})
            .sort_values(by=['customer_count','category1','category2'], ascending=[False,True,True])
           )








