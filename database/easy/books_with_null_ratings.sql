-- Oracle
/* Write your PL/SQL query statement below */
select book_id, title, author, published_year
  from books
 where rating is null
 order by book_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select book_id, title, author, published_year
  from books
 where rating is null
 order by book_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select book_id, title, author, published_year
  from books
 where rating is null
 order by book_id
;


# MySQL
# Write your MySQL query statement below
select book_id, title, author, published_year
  from books
 where rating is null
 order by book_id
;


# Pandas
import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    return books[books.rating.isna()].drop(columns='rating').sort_values('book_id')

