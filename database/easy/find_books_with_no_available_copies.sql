-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
           lb.total_copies, count(*) as current_borrowers
    from library_books lb
         inner join borrowing_records br on (br.book_id = lb.book_id and br.return_date is null)
    group by lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
    having lb.total_copies = count(*)
)
select book_id, title, author, genre, publication_year, current_borrowers
  from t
 order by current_borrowers desc, title
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
           lb.total_copies, count(*) as current_borrowers
    from library_books lb
         inner join borrowing_records br on (br.book_id = lb.book_id and br.return_date is null)
    group by lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
    having lb.total_copies = count(*)
)
select book_id, title, author, genre, publication_year, current_borrowers
  from t
 order by current_borrowers desc, title
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
           lb.total_copies, count(*) as current_borrowers
    from library_books lb
         inner join borrowing_records br on (br.book_id = lb.book_id and br.return_date is null)
    group by lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
    having lb.total_copies = count(*)
)
select book_id, title, author, genre, publication_year, current_borrowers
  from t
 order by current_borrowers desc, title
;


# MySQL
# Write your MySQL query statement below
with t as (
    select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
           lb.total_copies, count(*) as current_borrowers
    from library_books lb
         inner join borrowing_records br on (br.book_id = lb.book_id and br.return_date is null)
    group by lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
    having lb.total_copies = count(*)
)
select book_id, title, author, genre, publication_year, current_borrowers
  from t
 order by current_borrowers desc, title
;


# Pandas
import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    df = ( borrowing_records[borrowing_records['return_date'].isna()]
          .groupby('book_id', as_index=0)
          .size()
          .rename(columns={'size':'current_borrowers'})
         )
    return ( library_books
            .merge(df, how='inner', left_on=['book_id','total_copies'], right_on=['book_id','current_borrowers'])
            .drop('total_copies', axis=1)
            .sort_values(by=['current_borrowers','title'], ascending=[False,True])
           )





