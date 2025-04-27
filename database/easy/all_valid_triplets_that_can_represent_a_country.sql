-- Oracle
/* Write your PL/SQL query statement below */
select a.student_name as member_A,
       b.student_name as member_B,
       c.student_name as member_C
  from SchoolA a
       cross join SchoolB b
       cross join SchoolC c
 where a.student_id != b.student_id
   and a.student_name != b.student_name
   and b.student_id != c.student_id
   and b.student_name != c.student_name
   and c.student_id != a.student_id
   and c.student_name != a.student_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select a.student_name as member_A,
       b.student_name as member_B,
       c.student_name as member_C
  from SchoolA a
       cross join SchoolB b
       cross join SchoolC c
 where a.student_id != b.student_id
   and a.student_name != b.student_name
   and b.student_id != c.student_id
   and b.student_name != c.student_name
   and c.student_id != a.student_id
   and c.student_name != a.student_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select a.student_name as member_A,
       b.student_name as member_B,
       c.student_name as member_C
  from SchoolA a
       cross join SchoolB b
       cross join SchoolC c
 where a.student_id != b.student_id
   and a.student_name != b.student_name
   and b.student_id != c.student_id
   and b.student_name != c.student_name
   and c.student_id != a.student_id
   and c.student_name != a.student_name
;


# MySQL
# Write your MySQL query statement below
select a.student_name as member_A,
       b.student_name as member_B,
       c.student_name as member_C
  from SchoolA a
       cross join SchoolB b
       cross join SchoolC c
 where a.student_id != b.student_id
   and a.student_name != b.student_name
   and b.student_id != c.student_id
   and b.student_name != c.student_name
   and c.student_id != a.student_id
   and c.student_name != a.student_name
;


# Pandas
import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:
    return ( school_a
            .merge(school_b, how='cross')
            .merge(school_c, how='cross')
            .query('student_id_x   != student_id_y   and \
                    student_name_x != student_name_y and \
                    student_id_y   != student_id     and \
                    student_name_y != student_name   and \
                    student_id     != student_id_x   and \
                    student_name   != student_name_x'
                  )[['student_name_x','student_name_y','student_name']]
            .rename(columns={
                               'student_name_x': 'member_A',
                               'student_name_y': 'member_B',
                               'student_name'  : 'member_C'
                            }
                   )
           )

