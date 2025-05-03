-- Oracle
/* Write your PL/SQL query statement below */
select pp1.product_id as product1_id,
       pp2.product_id as product2_id,
       pi1.category as product1_category,
       pi2.category as product2_category,
       count(distinct pp1.user_id) as customer_count
  from ProductPurchases pp1
       inner join ProductPurchases pp2 on (pp2.product_id > pp1.product_id and pp2.user_id = pp1.user_id)
       inner join ProductInfo pi1 on (pi1.product_id = pp1.product_id)
       inner join ProductInfo pi2 on (pi2.product_id = pp2.product_id)
 group by pp1.product_id, pp2.product_id, pi1.category, pi2.category
having count(distinct pp1.user_id) >= 3
 order by customer_count desc, product1_id, product2_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select pp1.product_id as product1_id,
       pp2.product_id as product2_id,
       pi1.category as product1_category,
       pi2.category as product2_category,
       count(distinct pp1.user_id) as customer_count
  from ProductPurchases pp1
       inner join ProductPurchases pp2 on (pp2.product_id > pp1.product_id and pp2.user_id = pp1.user_id)
       inner join ProductInfo pi1 on (pi1.product_id = pp1.product_id)
       inner join ProductInfo pi2 on (pi2.product_id = pp2.product_id)
 group by pp1.product_id, pp2.product_id, pi1.category, pi2.category
having count(distinct pp1.user_id) >= 3
 order by customer_count desc, product1_id, product2_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select pp1.product_id as product1_id,
       pp2.product_id as product2_id,
       pi1.category as product1_category,
       pi2.category as product2_category,
       count(distinct pp1.user_id) as customer_count
  from ProductPurchases pp1
       inner join ProductPurchases pp2 on (pp2.product_id > pp1.product_id and pp2.user_id = pp1.user_id)
       inner join ProductInfo pi1 on (pi1.product_id = pp1.product_id)
       inner join ProductInfo pi2 on (pi2.product_id = pp2.product_id)
 group by pp1.product_id, pp2.product_id, pi1.category, pi2.category
having count(distinct pp1.user_id) >= 3
 order by customer_count desc, product1_id, product2_id
;


# MySQL
# Write your MySQL query statement below
select pp1.product_id as product1_id,
       pp2.product_id as product2_id,
       pi1.category as product1_category,
       pi2.category as product2_category,
       count(distinct pp1.user_id) as customer_count
  from ProductPurchases pp1
       inner join ProductPurchases pp2 on (pp2.product_id > pp1.product_id and pp2.user_id = pp1.user_id)
       inner join ProductInfo pi1 on (pi1.product_id = pp1.product_id)
       inner join ProductInfo pi2 on (pi2.product_id = pp2.product_id)
 group by pp1.product_id, pp2.product_id, pi1.category, pi2.category
having count(distinct pp1.user_id) >= 3
 order by customer_count desc, product1_id, product2_id
;


# Pandas
import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    return ( product_purchases
            .merge(product_purchases, how='inner', on='user_id')
            .query('product_id_x < product_id_y')
            .groupby(['product_id_x', 'product_id_y'], as_index=0)['user_id']
            .nunique()
            .query('user_id >= 3')
            .rename(columns={'product_id_x':'product1_id', 'product_id_y':'product2_id', 'user_id':'customer_count'})
            .merge(product_info, how='inner', left_on='product1_id', right_on='product_id')
            .merge(product_info, how='inner', left_on='product2_id', right_on='product_id')
            [['product1_id', 'product2_id', 'category_x', 'category_y', 'customer_count']]
            .rename(columns={'category_x': 'product1_category', 'category_y': 'product2_category'})
            .sort_values(by=['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])
           )

