-- Oracle
/* Write your PL/SQL query statement below */
with t (today) as (
    select DATE'2019-06-23' from dual
)
select b.book_id, b.name
  from books b
       cross join t
       left outer join orders o on (o.book_id = b.book_id and
                                    o.dispatch_date between add_months(t.today, -12) and t.today
                                   )
 where b.available_from < add_months(t.today, -1)
 group by b.book_id, b.name
 having coalesce(sum(o.quantity), 0) < 10
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (today) as (
    select '2019-06-23'::date
)
select b.book_id, b.name
  from books b
       cross join t
       left outer join orders o on (o.book_id = b.book_id and
                                    o.dispatch_date between t.today - interval '12' month and t.today
                                   )
 where b.available_from < t.today - interval '1' month
 group by b.book_id, b.name
 having coalesce(sum(o.quantity), 0) < 10
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (today) as (
    select '2019-06-23'
)
select b.book_id, b.name
  from books b
       cross join t
       left outer join orders o on (o.book_id = b.book_id and
                                    o.dispatch_date between dateadd(month, -12, t.today) and t.today
                                   )
 where b.available_from < dateadd(month, -1, t.today)
 group by b.book_id, b.name
 having coalesce(sum(o.quantity), 0) < 10
;


# MySQL
# Write your MySQL query statement below
with t (today) as (
    select '2019-06-23'
)
select b.book_id, b.name
  from books b
       cross join t
       left outer join orders o on (o.book_id = b.book_id and
                                    o.dispatch_date between t.today - interval '12' month and t.today
                                   )
 where b.available_from < t.today - interval '1' month
 group by b.book_id, b.name
 having coalesce(sum(o.quantity), 0) < 10
;


# Pandas
import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = ( orders
          .assign(to_date=pd.to_datetime('2019-06-23'),
                  from_date=pd.to_datetime('2019-06-23')-pd.DateOffset(years=1)
                 )
          .query('dispatch_date >= from_date and dispatch_date <= to_date')
          .groupby('book_id',as_index=False)['quantity']
          .sum()
         )
    return ( books
            .assign(cutoff_date=pd.to_datetime('2019-06-23')-pd.DateOffset(months=1))
            .query('available_from <= cutoff_date')
            .merge(df, how='left', on='book_id')
            .query('quantity.isnull() | quantity < 10')[['book_id','name']]
           )

