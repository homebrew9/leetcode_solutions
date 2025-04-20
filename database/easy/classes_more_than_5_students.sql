-- Oracle
/* Write your PL/SQL query statement below */
select class as "class"
from courses
group by class
having count(*) >= 5
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select class
  from courses
 group by class
having count(*) >= 5
;


-- SQL Server
/* Write your T-SQL query statement below */
select class as [class]
from courses
group by class
having count(*) >= 5
;


# MySQL
# Write your MySQL query statement below
select class
  from courses
 group by class
having count(distinct student) >= 5
;

# The following query used to fail earlier, but is now accepted.
# Write your MySQL query statement below
select class
  from courses
 group by class
having count(*) >= 5
;


# Pandas
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class', as_index=False).agg(student_count=('student','count'))
    return df[df['student_count'] >= 5][['class']]

