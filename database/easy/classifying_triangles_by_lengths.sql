-- Oracle
/* Write your PL/SQL query statement below */
select case when not (a + b > c and b + c > a and c + a > b) then 'Not A Triangle'
            when a = b and b = c and c = a then 'Equilateral'
            when a = b or b = c or c = a then 'Isosceles'
            else 'Scalene'
       end as triangle_type
from triangles
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select case when not (a + b > c and b + c > a and c + a > b) then 'Not A Triangle'
            when a = b and b = c and c = a then 'Equilateral'
            when a = b or b = c or c = a then 'Isosceles'
            else 'Scalene'
       end as triangle_type
from triangles
;


-- SQL Server


# MySQL
# Write your MySQL query statement below
select case when not (a + b > c and b + c > a and c + a > b) then 'Not A Triangle'
            when a = b and b = c and c = a then 'Equilateral'
            when a = b or b = c or c = a then 'Isosceles'
            else 'Scalene'
       end as triangle_type
from triangles
;


# Pandas
import pandas as pd

def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:
    triangles['triangle_type'] = triangles.apply(is_triangle, axis=1)
    return triangles[['triangle_type']]

def is_triangle(row):
    a, b, c = row
    if not (a + b > c and b + c > a and c + a > b):
        return 'Not A Triangle'
    if a == b == c:
        return 'Equilateral'
    if a == b or b == c or c == a:
        return 'Isosceles'
    return 'Scalene'

