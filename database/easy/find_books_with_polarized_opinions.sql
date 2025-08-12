-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
# MySQL
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

