-- Oracle
/* Write your PL/SQL query statement below */
select id, movie, description, rating
  from cinema
 where mod(id, 2) = 1
   and description != 'boring'
 order by rating desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select id, movie, description, rating
  from cinema
 where mod(id, 2) = 1
   and description != 'boring'
 order by rating desc
;


-- SQL Server
/* Write your T-SQL query statement below */
select id, movie, description, rating
  from cinema
 where id % 2 = 1
   and description != 'boring'
 order by rating desc
;


# MySQL
# Write your MySQL query statement below
select id, movie, description, rating
  from cinema
 where mod(id, 2) = 1
   and description != 'boring'
 order by rating desc
;


# Pandas
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return ( cinema[(cinema['id']%2 == 1) & (cinema['description'] != 'boring')]
            .sort_values(by='rating', ascending=False)
           )

