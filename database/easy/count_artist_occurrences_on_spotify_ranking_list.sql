-- Oracle
/* Write your PL/SQL query statement below */
select artist, count(*) as occurrences
from spotify
group by artist
order by occurrences desc, artist
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select artist, count(*) as occurrences
from spotify
group by artist
order by occurrences desc, artist
;


-- SQL Server
/* Write your T-SQL query statement below */
select artist, count(*) as occurrences
from spotify
group by artist
order by occurrences desc, artist
;


# MySQL
# Write your MySQL query statement below
select artist, count(*) as occurrences
from spotify
group by artist
order by occurrences desc, artist
;


# Pandas
import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    return (  spotify.groupby(by='artist', as_index=False)['id']
                     .count()
                     .rename(columns={'id':'occurrences'})[['artist','occurrences']]
                     .sort_values(by=['occurrences', 'artist'], ascending=[False, True])
           )

