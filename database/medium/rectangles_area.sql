-- Oracle
/* Write your PL/SQL query statement below */
select pt1.id as p1, pt2.id as p2,
       abs(pt1.x_value - pt2.x_value) * abs(pt1.y_value - pt2.y_value) as area
  from points pt1
       inner join points pt2 on (pt2.id > pt1.id)
 where pt1.x_value != pt2.x_value
   and pt1.y_value != pt2.y_value
 order by area desc, p1, p2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select pt1.id as p1, pt2.id as p2,
       abs(pt1.x_value - pt2.x_value) * abs(pt1.y_value - pt2.y_value) as area
  from points pt1
       inner join points pt2 on (pt2.id > pt1.id)
 where pt1.x_value != pt2.x_value
   and pt1.y_value != pt2.y_value
 order by area desc, p1, p2
;


-- SQL Server
/* Write your T-SQL query statement below */
select pt1.id as p1, pt2.id as p2,
       abs(pt1.x_value - pt2.x_value) * abs(pt1.y_value - pt2.y_value) as area
  from points pt1
       inner join points pt2 on (pt2.id > pt1.id)
 where pt1.x_value != pt2.x_value
   and pt1.y_value != pt2.y_value
 order by area desc, p1, p2
;


# MySQL
# Write your MySQL query statement below
select pt1.id as p1, pt2.id as p2,
       abs(pt1.x_value - pt2.x_value) * abs(pt1.y_value - pt2.y_value) as area
  from points pt1
       inner join points pt2 on (pt2.id > pt1.id)
 where pt1.x_value != pt2.x_value
   and pt1.y_value != pt2.y_value
 order by area desc, p1, p2
;


# Pandas
import pandas as pd

def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    df = ( points
          .merge(points, how='cross')
          .query('id_y > id_x and x_value_x != x_value_y and y_value_x != y_value_y')
         )
    return ( df
            .assign(area=abs(df['x_value_x'] - df['x_value_y'])*abs(df['y_value_x'] - df['y_value_y']))
            .rename(columns={'id_x':'p1', 'id_y':'p2'})[['p1','p2','area']]
            .sort_values(by=['area','p1','p2'], ascending=[False,True,True])
           )

