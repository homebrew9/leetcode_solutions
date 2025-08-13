-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select rs.book_id,
           count(*) over (partition by rs.book_id) as total_sessions,
           max(rs.session_rating) over (partition by rs.book_id) as highest_rating,
           min(rs.session_rating) over (partition by rs.book_id) as lowest_rating,
           max(rs.session_rating) over (partition by rs.book_id)
           - min(rs.session_rating) over (partition by rs.book_id) as rating_spread,
           case when rs.session_rating <= 2 or rs.session_rating >= 4 then 1 else 0 end as extreme_rating
      from reading_sessions rs
     where exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating >= 4
                  )
       and exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating <= 2
                  )
),
t1 as (
    select t.book_id,
           t.rating_spread,
           sum(t.extreme_rating) / count(*) as polarization_score
      from t
     where t.total_sessions >= 5
     group by t.book_id, t.rating_spread
    having sum(t.extreme_rating) / count(*) >= 0.6
)
select t1.book_id,
       b.title, b.author, b.genre, b.pages,
       t1.rating_spread,
       round(t1.polarization_score, 2) as polarization_score
  from t1
       inner join books b on (b.book_id = t1.book_id)
 order by t1.polarization_score desc, b.title desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select rs.book_id,
           count(*) over (partition by rs.book_id) as total_sessions,
           max(rs.session_rating) over (partition by rs.book_id) as highest_rating,
           min(rs.session_rating) over (partition by rs.book_id) as lowest_rating,
           max(rs.session_rating) over (partition by rs.book_id)
           - min(rs.session_rating) over (partition by rs.book_id) as rating_spread,
           case when rs.session_rating <= 2 or rs.session_rating >= 4 then 1 else 0 end as extreme_rating
      from reading_sessions rs
     where exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating >= 4
                  )
       and exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating <= 2
                  )
),
t1 as (
    select t.book_id,
           t.rating_spread,
           sum(t.extreme_rating)::numeric / count(*) as polarization_score
      from t
     where t.total_sessions >= 5
     group by t.book_id, t.rating_spread
    having sum(t.extreme_rating)::numeric / count(*) >= 0.6
)
select t1.book_id,
       b.title, b.author, b.genre, b.pages,
       t1.rating_spread,
       round(t1.polarization_score, 2) as polarization_score
  from t1
       inner join books b on (b.book_id = t1.book_id)
 order by t1.polarization_score desc, b.title desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select rs.book_id,
           count(*) over (partition by rs.book_id) as total_sessions,
           max(rs.session_rating) over (partition by rs.book_id) as highest_rating,
           min(rs.session_rating) over (partition by rs.book_id) as lowest_rating,
           max(rs.session_rating) over (partition by rs.book_id)
           - min(rs.session_rating) over (partition by rs.book_id) as rating_spread,
           case when rs.session_rating <= 2 or rs.session_rating >= 4 then 1 else 0 end as extreme_rating
      from reading_sessions rs
     where exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating >= 4
                  )
       and exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating <= 2
                  )
),
t1 as (
    select t.book_id,
           t.rating_spread,
           CONVERT(FLOAT, sum(t.extreme_rating)) / count(*) as polarization_score
      from t
     where t.total_sessions >= 5
     group by t.book_id, t.rating_spread
    having CONVERT(FLOAT, sum(t.extreme_rating)) / count(*) >= 0.6
)
select t1.book_id,
       b.title, b.author, b.genre, b.pages,
       t1.rating_spread,
       round(t1.polarization_score, 2) as polarization_score
  from t1
       inner join books b on (b.book_id = t1.book_id)
 order by t1.polarization_score desc, b.title desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select rs.book_id,
           count(*) over (partition by rs.book_id) as total_sessions,
           max(rs.session_rating) over (partition by rs.book_id) as highest_rating,
           min(rs.session_rating) over (partition by rs.book_id) as lowest_rating,
           max(rs.session_rating) over (partition by rs.book_id)
           - min(rs.session_rating) over (partition by rs.book_id) as rating_spread,
           case when rs.session_rating <= 2 or rs.session_rating >= 4 then 1 else 0 end as extreme_rating
      from reading_sessions rs
     where exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating >= 4
                  )
       and exists (select null
                     from reading_sessions rs1
                    where rs1.book_id = rs.book_id
                      and rs1.session_rating <= 2
                  )
),
t1 as (
    select t.book_id,
           t.rating_spread,
           sum(t.extreme_rating) / count(*) as polarization_score
      from t
     where t.total_sessions >= 5
     group by t.book_id, t.rating_spread
    having sum(t.extreme_rating) / count(*) >= 0.6
)
select t1.book_id,
       b.title, b.author, b.genre, b.pages,
       t1.rating_spread,
       round(t1.polarization_score, 2) as polarization_score
  from t1
       inner join books b on (b.book_id = t1.book_id)
 order by t1.polarization_score desc, b.title desc
;


# Pandas
import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    atleast_5_session_book_ids = reading_sessions.groupby('book_id', as_index=0).size().query('size >= 5')['book_id']
    atleast_one_lowest_rating_book_ids = reading_sessions.query('session_rating <= 2')['book_id']
    atleast_one_highest_rating_book_ids = reading_sessions.query('session_rating >= 4')['book_id']
    df = ( reading_sessions[(reading_sessions['book_id'].isin(atleast_5_session_book_ids)) & \
                            (reading_sessions['book_id'].isin(atleast_one_lowest_rating_book_ids)) & \
                            (reading_sessions['book_id'].isin(atleast_one_highest_rating_book_ids))
                           ]
         )
    df['extreme_rating'] = np.where((df['session_rating'] <= 2) | (df['session_rating'] >= 4), 1, 0)
    df1 = ( df
           .groupby('book_id', as_index=0)
           .agg(min_rating=('session_rating','min'), max_rating=('session_rating','max'), extreme_count=('extreme_rating','sum'), total_count=('session_id','count'))
          )
    df1['rating_spread'] = df1['max_rating'] - df1['min_rating']
    df1['polarization_score'] = df1['extreme_count'] / df1['total_count']
    df1['polarization_score'] = df1['polarization_score'].apply(round_half_up, p=2)
    df2 = df1.query('polarization_score >= 0.6')
    return ( df2
            .merge(books, how='inner', on='book_id')[['book_id','title','author','genre','pages','rating_spread', 'polarization_score']]
            .sort_values(by=['polarization_score','title'], ascending=[False,False])
           )

def round_half_up(n, p=0):
    # Custom function to fix "Banker's rounding" which is the default in Python
    # In Python: round(2.5) = 2, round(3.5) = 4 i.e. it returns the nearest even neighbor
    # round_half_up(2.5) = 3, round_half_up(3.5) = 4, round_half_up(0.625, 2) = 0.63
    v = 10**p
    return math.floor(n * v + 0.5) / v

