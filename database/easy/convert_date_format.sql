-- Oracle
/* Write your PL/SQL query statement below */
select to_char(day, 'fmDay, Month dd, yyyy') as day
from days
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select to_char(day, 'fmDay, fmMonth fmdd, yyyy') as day
from days
;


-- SQL Server
/* Write your T-SQL query statement below */
select format(day, 'dddd, MMMM d, yyyy') as day
from days
;


# MySQL
# Write your MySQL query statement below
select date_format(day, '%W, %M %e, %Y') as day
from days
;


# Pandas
import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    # Weird problem in Python's strftime: "%-d" strips leading zeros only in Linux, not in Windows!
    # https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
    
    return days['day'].dt.strftime('%A, %B %d, %Y').str.replace(' 0',' ').to_frame()

