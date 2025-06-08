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


# Pandas

