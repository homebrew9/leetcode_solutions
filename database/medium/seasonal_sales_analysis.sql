-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select case when to_char(s.sale_date, 'mon') in ('dec','jan','feb') then 'Winter'
                when to_char(s.sale_date, 'mon') in ('mar','apr','may') then 'Spring'
                when to_char(s.sale_date, 'mon') in ('jun','jul','aug') then 'Summer'
                else 'Fall'
        end as season,
        p.category,
        sum(s.quantity) as total_quantity, sum(s.quantity * s.price) as total_revenue
    from sales s
        inner join products p on (p.product_id = s.product_id)
    group by case when to_char(s.sale_date, 'mon') in ('dec','jan','feb') then 'Winter'
                  when to_char(s.sale_date, 'mon') in ('mar','apr','may') then 'Spring'
                  when to_char(s.sale_date, 'mon') in ('jun','jul','aug') then 'Summer'
                  else 'Fall'
             end, p.category
),
t1 as (
    select season, category, total_quantity, total_revenue,
           dense_rank() over (partition by season order by total_quantity desc, total_revenue desc) as drnk
    from t
)
select season, category, total_quantity, total_revenue
  from t1
 where drnk = 1
 order by season
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select case when to_char(s.sale_date, 'mon') in ('dec','jan','feb') then 'Winter'
                when to_char(s.sale_date, 'mon') in ('mar','apr','may') then 'Spring'
                when to_char(s.sale_date, 'mon') in ('jun','jul','aug') then 'Summer'
                else 'Fall'
        end as season,
        p.category,
        sum(s.quantity) as total_quantity, sum(s.quantity * s.price) as total_revenue
    from sales s
        inner join products p on (p.product_id = s.product_id)
    group by case when to_char(s.sale_date, 'mon') in ('dec','jan','feb') then 'Winter'
                  when to_char(s.sale_date, 'mon') in ('mar','apr','may') then 'Spring'
                  when to_char(s.sale_date, 'mon') in ('jun','jul','aug') then 'Summer'
                  else 'Fall'
             end, p.category
),
t1 as (
    select season, category, total_quantity, total_revenue,
           dense_rank() over (partition by season order by total_quantity desc, total_revenue desc) as drnk
    from t
)
select season, category, total_quantity, total_revenue
  from t1
 where drnk = 1
 order by season
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select case when convert(varchar(3), s.sale_date, 7) in ('dec','jan','feb') then 'Winter'
                when convert(varchar(3), s.sale_date, 7) in ('mar','apr','may') then 'Spring'
                when convert(varchar(3), s.sale_date, 7) in ('jun','jul','aug') then 'Summer'
                else 'Fall'
        end as season,
        p.category,
        sum(s.quantity) as total_quantity, sum(s.quantity * s.price) as total_revenue
    from sales s
        inner join products p on (p.product_id = s.product_id)
    group by case when convert(varchar(3), s.sale_date, 7) in ('dec','jan','feb') then 'Winter'
                  when convert(varchar(3), s.sale_date, 7) in ('mar','apr','may') then 'Spring'
                  when convert(varchar(3), s.sale_date, 7) in ('jun','jul','aug') then 'Summer'
                  else 'Fall'
             end, p.category
),
t1 as (
    select season, category, total_quantity, total_revenue,
           dense_rank() over (partition by season order by total_quantity desc, total_revenue desc) as drnk
    from t
)
select season, category, total_quantity, total_revenue
  from t1
 where drnk = 1
 order by season
;


# MySQL
# Write your MySQL query statement below
with t as (
    select case when date_format(s.sale_date, '%b') in ('dec','jan','feb') then 'Winter'
                when date_format(s.sale_date, '%b') in ('mar','apr','may') then 'Spring'
                when date_format(s.sale_date, '%b') in ('jun','jul','aug') then 'Summer'
                else 'Fall'
        end as season,
        p.category,
        sum(s.quantity) as total_quantity, sum(s.quantity * s.price) as total_revenue
    from sales s
        inner join products p on (p.product_id = s.product_id)
    group by case when date_format(s.sale_date, '%b') in ('dec','jan','feb') then 'Winter'
                  when date_format(s.sale_date, '%b') in ('mar','apr','may') then 'Spring'
                  when date_format(s.sale_date, '%b') in ('jun','jul','aug') then 'Summer'
                  else 'Fall'
             end, p.category
),
t1 as (
    select season, category, total_quantity, total_revenue,
           dense_rank() over (partition by season order by total_quantity desc, total_revenue desc) as drnk
    from t
)
select season, category, total_quantity, total_revenue
  from t1
 where drnk = 1
 order by season
;


# Pandas
import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['month'] = sales['sale_date'].dt.strftime('%b')
    sales['season'] = np.where(sales['month'].isin(['Dec','Jan','Feb']), 'Winter',
                               np.where(sales['month'].isin(['Mar','Apr','May']), 'Spring',
                                        np.where(sales['month'].isin(['Jun','Jul','Aug']), 'Summer', 'Fall'
                                        )
                               )
                      )
    sales['revenue'] = sales['quantity'] * sales['price']
    df = ( sales
          .merge(products, how='inner', on='product_id')
          .groupby(['season','category'], as_index=0)
          .agg(total_quantity=('quantity','sum'), total_revenue=('revenue','sum'))
         )
    # In order to do "partition by x order by y, z", we first combine [y,z] into a single combined column
    df['combined'] = list(zip(df['total_quantity'],df['total_revenue']))
    df['drnk'] = ( df
                  .groupby('season', as_index=0)['combined']
                  .rank(method='dense',ascending=False).astype(int)
                 )
    return df[df['drnk']==1][['season','category','total_quantity','total_revenue']].sort_values('season')


