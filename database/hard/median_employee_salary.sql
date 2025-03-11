-- Oracle
/* Write your PL/SQL query statement below */
with t (id, company, salary, cnt, rnum) as (
select id, company, salary,
       count(*) over (partition by company) as cnt,
       row_number() over (partition by company order by salary, id) as rnum
from employee
),
t1 (id, company, salary, cnt, rnum, from_num, to_num) as (
select id, company, salary, cnt, rnum,
       case when mod(cnt, 2) = 1 then ceil(cnt/2) else cnt/2 end as from_num,
       case when mod(cnt, 2) = 1 then ceil(cnt/2) else cnt/2 + 1 end as to_num
from t
)
select id, company, salary
from t1
where rnum between from_num and to_num
order by company, rnum
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (id, company, salary, cnt, rnum) as (
select id, company, salary,
       count(*) over (partition by company) as cnt,
       row_number() over (partition by company order by salary, id) as rnum
from employee
),
t1 (id, company, salary, cnt, rnum, from_num, to_num) as (
select id, company, salary, cnt, rnum,
       case when mod(cnt, 2) = 1 then ceil(cnt::numeric/2) else cnt::numeric/2 end as from_num,
       case when mod(cnt, 2) = 1 then ceil(cnt::numeric/2) else cnt::numeric/2 + 1 end as to_num
from t
)
select id, company, salary
from t1
where rnum between from_num and to_num
order by company, rnum
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (id, company, salary, cnt, rnum) as (
select id, company, salary,
       count(*) over (partition by company) as cnt,
       row_number() over (partition by company order by salary, id) as rnum
from employee
),
t1 (id, company, salary, cnt, rnum, from_num, to_num) as (
select id, company, salary, cnt, rnum,
       case when cnt % 2 = 1 then ceiling(convert(float, cnt)/2) else cnt/2 end as from_num,
       case when cnt % 2 = 1 then ceiling(convert(float, cnt)/2) else cnt/2 + 1 end as to_num
from t
)
select id, company, salary
from t1
where rnum between from_num and to_num
order by company, rnum
;


# MySQL
# Write your MySQL query statement below
with t (id, company, salary, cnt, rnum) as (
select id, company, salary,
       count(*) over (partition by company) as cnt,
       row_number() over (partition by company order by salary, id) as rnum
from employee
),
t1 (id, company, salary, cnt, rnum, from_num, to_num) as (
select id, company, salary, cnt, rnum,
       case when mod(cnt, 2) = 1 then ceil(cnt/2) else cnt/2 end as from_num,
       case when mod(cnt, 2) = 1 then ceil(cnt/2) else cnt/2 + 1 end as to_num
from t
)
select id, company, salary
from t1
where rnum between from_num and to_num
order by company, rnum
;


# Pandas
import pandas as pd

def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(['company','salary'], inplace=True)
    df = ( employee
          .assign(cnt=employee.groupby('company')['id'].transform('count'),
                  rn=employee.groupby('company').cumcount()+1
                 )
         )
    df = df.assign(from_num=np.where(df['cnt']%2==1, df['cnt']/2+0.5, df['cnt']//2),
                   to_num=np.where(df['cnt']%2==1, df['cnt']/2+0.5, df['cnt']//2+1)
                  )
    return df[(df['rn']>=df['from_num']) & (df['rn']<=df['to_num'])][['id','company','salary']]

