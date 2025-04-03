-- Oracle
/* Write your PL/SQL query statement below */
select round(min(sqrt(power((p2.x - p1.x), 2) + power((p2.y - p1.y), 2))), 2) as shortest
from point2d p1
     cross join point2d p2
where not(p1.x = p2.x and p1.y = p2.y)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select /*p1.x as p1_x, p1.y as p1_y,
       p2.x as p2_x, p2.y as p2_y,
       (p2.x - p1.x) as xdiff, (p2.y - p1.y) as ydiff,
       power((p2.x - p1.x), 2) as xdiffsq, power((p2.y - p1.y), 2) as ydiffsq,*/
       round(min(sqrt(power((p2.x - p1.x), 2) + power((p2.y - p1.y), 2)))::numeric, 2) as shortest
from point2d p1
     cross join point2d p2
where not(p1.x = p2.x and p1.y = p2.y)
;


-- SQL Server
/* Write your T-SQL query statement below */
select round(min(sqrt(power((p2.x - p1.x), 2) + power((p2.y - p1.y), 2))), 2) as shortest
from point2d p1
     cross join point2d p2
where p1.x != p2.x or p1.y != p2.y
;


# MySQL
# Write your MySQL query statement below
select round(min(sqrt(power((p2.x - p1.x), 2) + power((p2.y - p1.y), 2))), 2) as shortest
from point2d p1
     cross join point2d p2
where p1.x != p2.x or p1.y != p2.y
;


# Pandas
import pandas as pd

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    df = point2_d.merge(point2_d, how='cross').query('x_x != x_y | y_x != y_y')
    df['dist'] = round(pow((df['x_y'] - df['x_x'])**2 + (df['y_y'] - df['y_x'])**2, 0.5), 2)
    return pd.DataFrame(data={'shortest': [df['dist'].min()]})

