-- Oracle
/* Write your PL/SQL query statement below */
select country, gold_medals, silver_medals, bronze_medals
  from olympic
 order by gold_medals desc, silver_medals desc, bronze_medals desc, country
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select country, gold_medals, silver_medals, bronze_medals
  from olympic
 order by gold_medals desc, silver_medals desc, bronze_medals desc, country
;


-- SQL Server
/* Write your T-SQL query statement below */
select country, gold_medals, silver_medals, bronze_medals
  from olympic
 order by gold_medals desc, silver_medals desc, bronze_medals desc, country
;


# MySQL
# Write your MySQL query statement below
select country, gold_medals, silver_medals, bronze_medals
  from olympic
 order by gold_medals desc, silver_medals desc, bronze_medals desc, country
;


# Pandas
import pandas as pd

def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    return olympic.sort_values(by=['gold_medals','silver_medals','bronze_medals','country'], ascending=[0,0,0,1])

