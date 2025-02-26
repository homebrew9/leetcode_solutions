-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select id, month, salary,
           sum(salary) over (partition by id
                             order by month range between 2 preceding and current row
                            ) as cumulative_salary,
           max(month) over (partition by id) as most_recent_month
      from employee
)
select id, month, cumulative_salary as salary
  from t
 where month != most_recent_month
 order by id, month desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, month, salary,
           sum(salary) over (partition by id
                             order by month range between 2 preceding and current row
                            ) as cumulative_salary,
           max(month) over (partition by id) as most_recent_month
      from employee
)
select id, month, cumulative_salary as salary
  from t
 where month != most_recent_month
 order by id, month desc
;


-- SQL Server
/* Write your T-SQL query statement below */
--
-- In SQL Server, RANGE is only supported with unbounded preceding and current row window frame delimiters
-- https://learn.microsoft.com/en-us/answers/questions/1350730/range-is-only-supported-with-unbounded-and-current
--
select e1.id, e1.month, e1.salary + isnull(e2.salary, 0) + isnull(e3.salary, 0) as salary
  from employee e1
       left outer join employee e2 on (e2.id = e1.id and e2.month = e1.month - 1)
       left outer join employee e3 on (e3.id = e2.id and e3.month = e2.month - 1)
 where e1.month < (select max(x.month) from employee x where x.id = e1.id)
 order by e1.id, e1.month desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select id, month, salary,
           sum(salary) over (partition by id
                             order by month range between 2 preceding and current row
                            ) as cumulative_salary,
           max(month) over (partition by id) as most_recent_month
      from employee
)
select id, month, cumulative_salary as salary
  from t
 where month != most_recent_month
 order by id, month desc
;


# Pandas
import pandas as pd

def cumulative_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(['id','month'], inplace=True)
    df = ( employee
          .assign(prev_id=employee['id'].shift(1),
                  prev_month=employee['month'].shift(1),
                  prev_salary=employee['salary'].shift(1),
                  pp_id=employee['id'].shift(2),
                  pp_month=employee['month'].shift(2),
                  pp_salary=employee['salary'].shift(2)
                 )
          .fillna(0)
         )
    df['cumulative_sal'] = ( df['salary'] 
                             +
                             np.where((df['prev_id'] == df['id']) & (df['prev_month'] == df['month']-1),
                                      df['prev_salary'], 0)
                             +
                             np.where((df['pp_id'] == df['id']) & (df['pp_month'] == df['month']-2),
                                      df['pp_salary'], 0)
                           )
    df1 = ( employee
           .groupby('id',as_index=0)['month']
           .max()
           .rename(columns={'month':'max_month'})
          )
    return ( df
            .merge(df1, how='left', on='id')
            .query('month != max_month')[['id','month','cumulative_sal']]
            .rename(columns={'cumulative_sal': 'salary'})
            .sort_values(by=['id','month'], ascending=[True,False])
           )

