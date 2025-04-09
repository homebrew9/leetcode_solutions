-- Oracle
/* Write your PL/SQL query statement below */
select sum(b.apple_count + coalesce(c.apple_count, 0)) as apple_count,
       sum(b.orange_count + coalesce(c.orange_count, 0)) as orange_count
from boxes b
     left outer join chests c on (c.chest_id = b.chest_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select sum(b.apple_count + coalesce(c.apple_count, 0)) as apple_count,
       sum(b.orange_count + coalesce(c.orange_count, 0)) as orange_count
from boxes b
     left outer join chests c on (c.chest_id = b.chest_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select sum(b.apple_count + coalesce(c.apple_count, 0)) as apple_count,
       sum(b.orange_count + coalesce(c.orange_count, 0)) as orange_count
from boxes b
     left outer join chests c on (c.chest_id = b.chest_id)
;


# MySQL
# Write your MySQL query statement below
select sum(b.apple_count + coalesce(c.apple_count, 0)) as apple_count,
       sum(b.orange_count + coalesce(c.orange_count, 0)) as orange_count
from boxes b
     left outer join chests c on (c.chest_id = b.chest_id)
;


# Pandas
import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:
    df = boxes.merge(chests, how='left', on='chest_id').fillna(0)
    df['apple_count'] = df['apple_count_x'] + df['apple_count_y']
    df['orange_count'] = df['orange_count_x'] + df['orange_count_y']
    return ( pd
            .DataFrame(data={'apple_count': [df[['apple_count']].sum().item()],
                             'orange_count': [df[['orange_count']].sum().item()]
                            }
                      )
           )

