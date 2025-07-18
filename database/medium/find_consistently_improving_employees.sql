-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select e.employee_id, e.name, pr.review_date, pr.rating,
        dense_rank() over (partition by e.employee_id order by pr.review_date desc) as drnk,
        count(*) over (partition by e.employee_id) as review_count
    from employees e
        inner join performance_reviews pr on (pr.employee_id = e.employee_id)
),
t1 as (
    select employee_id, name, review_date, rating, drnk,
        case when lag(rating) over (partition by employee_id order by review_date desc) is null then 1
                when rating < lag(rating) over (partition by employee_id order by review_date desc) then 1
                else 0
        end as rating_diff,
        case when review_date = max(review_date) over (partition by employee_id) then rating end as latest_rating,
        case when review_date = min(review_date) over (partition by employee_id) then rating end as earliest_rating
    from t
    where review_count >= 3
    and drnk <= 3
),
t2 as (
    select employee_id, name, sum(rating_diff) as rating_diff_total,
        max(latest_rating) - max(earliest_rating) as improvement_score
    from t1
    group by employee_id, name
    having sum(rating_diff) = 3
)
select employee_id, name, improvement_score
  from t2
 order by improvement_score desc, name asc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select e.employee_id, e.name, pr.review_date, pr.rating,
        dense_rank() over (partition by e.employee_id order by pr.review_date desc) as drnk,
        count(*) over (partition by e.employee_id) as review_count
    from employees e
        inner join performance_reviews pr on (pr.employee_id = e.employee_id)
),
t1 as (
    select employee_id, name, review_date, rating, drnk,
        case when lag(rating) over (partition by employee_id order by review_date desc) is null then 1
                when rating < lag(rating) over (partition by employee_id order by review_date desc) then 1
                else 0
        end as rating_diff,
        case when review_date = max(review_date) over (partition by employee_id) then rating end as latest_rating,
        case when review_date = min(review_date) over (partition by employee_id) then rating end as earliest_rating
    from t
    where review_count >= 3
    and drnk <= 3
),
t2 as (
    select employee_id, name, sum(rating_diff) as rating_diff_total,
        max(latest_rating) - max(earliest_rating) as improvement_score
    from t1
    group by employee_id, name
    having sum(rating_diff) = 3
)
select employee_id, name, improvement_score
  from t2
 order by improvement_score desc, name asc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select e.employee_id, e.name, pr.review_date, pr.rating,
        dense_rank() over (partition by e.employee_id order by pr.review_date desc) as drnk,
        count(*) over (partition by e.employee_id) as review_count
    from employees e
        inner join performance_reviews pr on (pr.employee_id = e.employee_id)
),
t1 as (
    select employee_id, name, review_date, rating, drnk,
        case when lag(rating) over (partition by employee_id order by review_date desc) is null then 1
                when rating < lag(rating) over (partition by employee_id order by review_date desc) then 1
                else 0
        end as rating_diff,
        case when review_date = max(review_date) over (partition by employee_id) then rating end as latest_rating,
        case when review_date = min(review_date) over (partition by employee_id) then rating end as earliest_rating
    from t
    where review_count >= 3
    and drnk <= 3
),
t2 as (
    select employee_id, name, sum(rating_diff) as rating_diff_total,
        max(latest_rating) - max(earliest_rating) as improvement_score
    from t1
    group by employee_id, name
    having sum(rating_diff) = 3
)
select employee_id, name, improvement_score
  from t2
 order by improvement_score desc, name asc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select e.employee_id, e.name, pr.review_date, pr.rating,
        dense_rank() over (partition by e.employee_id order by pr.review_date desc) as drnk,
        count(*) over (partition by e.employee_id) as review_count
    from employees e
        inner join performance_reviews pr on (pr.employee_id = e.employee_id)
),
t1 as (
    select employee_id, name, review_date, rating, drnk,
        case when lag(rating) over (partition by employee_id order by review_date desc) is null then 1
                when rating < lag(rating) over (partition by employee_id order by review_date desc) then 1
                else 0
        end as rating_diff,
        case when review_date = max(review_date) over (partition by employee_id) then rating end as latest_rating,
        case when review_date = min(review_date) over (partition by employee_id) then rating end as earliest_rating
    from t
    where review_count >= 3
    and drnk <= 3
),
t2 as (
    select employee_id, name, sum(rating_diff) as rating_diff_total,
        max(latest_rating) - max(earliest_rating) as improvement_score
    from t1
    group by employee_id, name
    having sum(rating_diff) = 3
)
select employee_id, name, improvement_score
  from t2
 order by improvement_score desc, name asc
;


# Pandas
import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    performance_reviews['drnk'] = ( performance_reviews
                                   .groupby('employee_id',as_index=0)['review_date']
                                   .rank(method='dense', ascending=False)
                                  )
    df = ( performance_reviews[performance_reviews['drnk']==1]
          .merge(performance_reviews[performance_reviews['drnk']==2], how='inner', on='employee_id')
          .query('rating_y < rating_x')
          .merge(performance_reviews[performance_reviews['drnk']==3], how='inner', on='employee_id')
          .query('rating < rating_y')
         )
    df['improvement_score'] = df['rating_x'] - df['rating']
    return ( df[['employee_id', 'improvement_score']]
            .merge(employees, how='inner', on='employee_id')[['employee_id','name','improvement_score']]
            .sort_values(by=['improvement_score', 'name'], ascending=[False, True])
           )

