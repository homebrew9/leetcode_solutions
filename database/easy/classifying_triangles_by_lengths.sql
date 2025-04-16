-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


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

