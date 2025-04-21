-- Oracle
/* Write your PL/SQL query statement below */
select name, population, area
from world
where area >= 3000000 or population >= 25000000
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select name, population, area
  from world
 where area >= 3000000
    or population >= 25000000
;


-- SQL Server
/* Write your T-SQL query statement below */
select name, population, area
  from world
 where area >= 3000000
    or population >= 25000000
;


# MySQL
# Write your MySQL query statement below
select name, population, area
  from world
where area >= 3000000
   or population >= 25000000
;


# Pandas
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area'] >= 3_000_000) | (world['population'] >= 25_000_000)][['name','population','area']]

