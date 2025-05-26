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


# Pandas

