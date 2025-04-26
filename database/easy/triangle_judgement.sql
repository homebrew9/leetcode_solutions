-- Oracle
/* Write your PL/SQL query statement below */
select x, y, z,
       case when x + y > z and y + z > x and z + x > y then 'Yes' else 'No' end as triangle
from triangle
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select x, y, z,
       case
           when x + y > z and y + z > x and z + x > y then 'Yes' else 'No'
       end as triangle
  from triangle
;


-- SQL Server
/* Write your T-SQL query statement below */
select x, y, z,
       case
           when x + y > z and y + z > x and z + x > y then 'Yes' else 'No'
       end as triangle
  from triangle
;


# MySQL
# Write your MySQL query statement below
select x, y, z,
       case
           when x + y > z and y + z > x and z + x > y then 'Yes' else 'No'
       end as triangle
  from triangle
;


# Pandas
import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = np.where(
        (triangle.x + triangle.y > triangle.z) &
        (triangle.y + triangle.z > triangle.x) &
        (triangle.z + triangle.x > triangle.y), 'Yes', 'No')
    return triangle

