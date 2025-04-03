-- Oracle
/* Write your PL/SQL query statement below */
with t (category, accounts_count) as (
select case when income < 20000 then 'Low Salary'
            when income between 20000 and 50000 then 'Average Salary'
            else 'High Salary'
       end as category,
       count(*) as accounts_count
from Accounts
group by case when income < 20000 then 'Low Salary'
            when income between 20000 and 50000 then 'Average Salary'
            else 'High Salary'
         end
),
t_catg (category) as (
select 'Low Salary' from dual union all
select 'Average Salary' from dual union all
select 'High Salary' from dual
)
select c.category, nvl(t.accounts_count, 0) as accounts_count
from t_catg c
     left outer join t on (t.category = c.category)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (category) as (
    select 'Low Salary' union all
    select 'Average Salary' union all
    select 'High Salary'
),
t1 (category, accounts_count) as (
    select case when income < 20000 then 'Low Salary'
                when income <= 50000 then 'Average Salary'
                else 'High Salary'
           end as category,
           count(*) as accounts_count
      from accounts
     group by case when income < 20000 then 'Low Salary'
                   when income <= 50000 then 'Average Salary'
                   else 'High Salary'
              end
)
select t.category, coalesce(t1.accounts_count, 0) as accounts_count
  from t
       left outer join t1 on (t1.category = t.category)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (category) as (
    select 'Low Salary' union all
    select 'Average Salary' union all
    select 'High Salary'
),
t1 (category, accounts_count) as (
    select case when income < 20000 then 'Low Salary'
                when income <= 50000 then 'Average Salary'
                else 'High Salary'
           end as category,
           count(*) as accounts_count
      from accounts
     group by case when income < 20000 then 'Low Salary'
                   when income <= 50000 then 'Average Salary'
                   else 'High Salary'
              end
)
select t.category, coalesce(t1.accounts_count, 0) as accounts_count
  from t
       left outer join t1 on (t1.category = t.category)
;


# MySQL
# Write your MySQL query statement below
with t (category) as (
    select 'Low Salary' union all
    select 'Average Salary' union all
    select 'High Salary'
),
t1 (category, accounts_count) as (
    select case when income < 20000 then 'Low Salary'
                when income <= 50000 then 'Average Salary'
                else 'High Salary'
           end as category,
           count(*) as accounts_count
      from accounts
     group by case when income < 20000 then 'Low Salary'
                   when income <= 50000 then 'Average Salary'
                   else 'High Salary'
              end
)
select t.category, coalesce(t1.accounts_count, 0) as accounts_count
  from t
       left outer join t1 on (t1.category = t.category)
;


# Pandas
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category'] = np.where(accounts['income'] < 20000,
                                    'Low Salary',
                                    np.where(accounts['income'] > 50000, 'High Salary', 'Average Salary')
                                   )
    df = accounts.groupby(by='category',as_index=False).agg(accounts_count=('category','count'))
    catg = pd.DataFrame(data={'category': ['Low Salary','Average Salary', 'High Salary']})
    return pd.merge(catg, df, how='left', on='category').fillna(0)

