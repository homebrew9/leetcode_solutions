-- Oracle
/* Write your PL/SQL query statement below */
select m.symbol as metal, n.symbol as nonmetal
from elements m
     cross join elements n
where m.type = 'Metal'
and n.type = 'Nonmetal'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select m.symbol as metal, n.symbol as nonmetal
from elements m
     cross join elements n
where m.type = 'Metal'
and n.type = 'Nonmetal'
;


-- SQL Server
/* Write your T-SQL query statement below */
select m.symbol as metal, n.symbol as nonmetal
from elements m
     cross join elements n
where m.type = 'Metal'
and n.type = 'Nonmetal'
;


# MySQL
# Write your MySQL query statement below
select m.symbol as metal, n.symbol as nonmetal
from elements m
     cross join elements n
where m.type = 'Metal'
and n.type = 'Nonmetal'
;


# Pandas
import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    return (  elements.merge(elements, how='cross')
                      .query("type_x == 'Metal' and type_y == 'Nonmetal'")[['symbol_x','symbol_y']]
                      .rename(columns={'symbol_x':'metal', 'symbol_y':'nonmetal'})
           )

