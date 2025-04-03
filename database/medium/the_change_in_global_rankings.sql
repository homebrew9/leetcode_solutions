-- Oracle
/* Write your PL/SQL query statement below */
select tp.team_id, tp.name,
       rank() over (order by tp.points desc, tp.name)
       - rank() over (order by (tp.points + pc.points_change) desc, tp.name) as rank_diff
from TeamPoints tp
     inner join PointsChange pc on (pc.team_id = tp.team_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select tp.team_id, tp.name,
       rank() over (order by tp.points desc, tp.name)
       - rank() over (order by (tp.points + pc.points_change) desc, tp.name) as rank_diff
from TeamPoints tp
     inner join PointsChange pc on (pc.team_id = tp.team_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select tp.team_id, tp.name,
       rank() over (order by tp.points desc, tp.name)
       - rank() over (order by (tp.points + pc.points_change) desc, tp.name) as rank_diff
from TeamPoints tp
     inner join PointsChange pc on (pc.team_id = tp.team_id)
;


# MySQL
# Write your MySQL query statement below
# Adding 0.0 converts orig_rank to a float. Otherwise, the following error is thrown:
# BIGINT UNSIGNED value is out of range in '(`rank() OVER ... - `rank() OVER ...'
# See the following links to understand this quirk of MySQL:
# https://stackoverflow.com/questions/12126991/cast-from-varchar-to-int-mysql
# https://dev.mysql.com/doc/refman/8.4/en/out-of-range-and-overflow.html
select tp.team_id, tp.name,
       rank() over (order by tp.points desc, tp.name) + 0.0
       - rank() over (order by (tp.points + pc.points_change) desc, tp.name) as rank_diff
from TeamPoints tp
     inner join PointsChange pc on (pc.team_id = tp.team_id)
;


# Pandas
import pandas as pd

def global_ratings_change(team_points: pd.DataFrame, points_change: pd.DataFrame) -> pd.DataFrame:
    df = team_points.merge(points_change, how='inner', on='team_id')
    df['upd_points'] = df['points'] + df['points_change']
    df = df.sort_values(['points','name'], ascending=[False,True]).reset_index(drop=True)
    df['orig_rank'] = df.index + 1
    df = df.sort_values(['upd_points','name'], ascending=[False,True]).reset_index(drop=True)
    df['upd_rank'] = df.index + 1
    df['rank_diff'] = df['orig_rank'] - df['upd_rank']
    return df[['team_id', 'name', 'rank_diff']]

