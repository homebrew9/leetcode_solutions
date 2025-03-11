-- Oracle
/* Write your PL/SQL query statement below */
with t_america as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'America'
),
t_asia as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Asia'
),
t_europe as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Europe'
),
t_hier (id) as (
    select 1 as id
      from dual
    union all
    select th.id + 1
      from t_hier th
     where th.id + 1 <= (  select max(x.drnk)
                             from (select max(drnk) as drnk from t_america union all
                                   select max(drnk) from t_asia union all
                                   select max(drnk) from t_europe
                                  ) x
                        )

)
select amer.name as America, asia.name as Asia, euro.name as Europe
  from t_hier th
       left outer join t_america amer on (amer.drnk = th.id)
       left outer join t_asia asia on (asia.drnk = th.id)
       left outer join t_europe euro on (euro.drnk = th.id)
 order by th.id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t_america as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'America'
),
t_asia as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Asia'
),
t_europe as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Europe'
),
t_hier (id) as (
    select 1 as id
    union all
    select th.id + 1
      from t_hier th
     where th.id + 1 <= (  select max(x.drnk)
                             from (select max(drnk) as drnk from t_america union all
                                   select max(drnk) from t_asia union all
                                   select max(drnk) from t_europe
                                  ) x
                        )

)
select amer.name as America, asia.name as Asia, euro.name as Europe
  from t_hier th
       left outer join t_america amer on (amer.drnk = th.id)
       left outer join t_asia asia on (asia.drnk = th.id)
       left outer join t_europe euro on (euro.drnk = th.id)
 order by th.id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_america as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'America'
),
t_asia as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Asia'
),
t_europe as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Europe'
),
t_max_drnk (max_length) as (
    select max(x.drnk)
     from (select max(drnk) as drnk from t_america union all
           select max(drnk) from t_asia union all
           select max(drnk) from t_europe
          ) x
),
t_hier (id) as (
    select 1 as id
    union all
    select th.id + 1
      from t_hier th
     where th.id + 1 <= (select max_length from t_max_drnk)

)
select amer.name as America, asia.name as Asia, euro.name as Europe
  from t_hier th
       left outer join t_america amer on (amer.drnk = th.id)
       left outer join t_asia asia on (asia.drnk = th.id)
       left outer join t_europe euro on (euro.drnk = th.id)
 order by th.id
option(maxrecursion 0)
;


# MySQL
# Write your MySQL query statement below
with recursive t_america as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'America'
),
t_asia as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Asia'
),
t_europe as (
    select name, row_number() over (order by name) as drnk
      from student
     where continent = 'Europe'
),
t_max_drnk (max_length) as (
    select max(x.drnk)
     from (select max(drnk) as drnk from t_america union all
           select max(drnk) from t_asia union all
           select max(drnk) from t_europe
          ) x
),
t_hier (id) as (
    select 1 as id
    union all
    select th.id + 1
      from t_hier th
     where th.id + 1 <= (select max_length from t_max_drnk)

)
select amer.name as America, asia.name as Asia, euro.name as Europe
  from t_hier th
       left outer join t_america amer on (amer.drnk = th.id)
       left outer join t_asia asia on (asia.drnk = th.id)
       left outer join t_europe euro on (euro.drnk = th.id)
 order by th.id
;


# Pandas
import pandas as pd

def geography_report(student: pd.DataFrame) -> pd.DataFrame:
    amer = student[student['continent']=='America'].sort_values('name')['name'].tolist()
    asia = student[student['continent']=='Asia'].sort_values('name')['name'].tolist()
    euro = student[student['continent']=='Europe'].sort_values('name')['name'].tolist()

    max_len = max(map(lambda x: len(x), (amer,asia,euro)))

    amer = amer + [np.NaN]*(max_len - len(amer))
    asia = asia + [np.NaN]*(max_len - len(asia))
    euro = euro + [np.NaN]*(max_len - len(euro))

    return pd.DataFrame(data={'America': amer, 'Asia': asia, 'Europe': euro})

