-- Oracle
/* Write your PL/SQL query statement below */
-- Using hierarchical queries to determine prev_max and next_max
with t (id, height, prev_max) as (
    select id, height, to_number(NULL) as prev_max
      from heights
     where id = (select min(id) from heights)
   union all
   select h.id, h.height, greatest(t.height, nvl(t.prev_max, 0))
     from t
          inner join heights h on (h.id = t.id + 1)
),
t1 (id, height, next_max) as (
    select id, height, to_number(NULL) as next_max
      from heights
     where id = (select max(id) from heights)
    union all
    select h.id, h.height, greatest(t1.height, nvl(t1.next_max, 0))
      from t1
           inner join heights h on (h.id = t1.id - 1)
),
t2 (id, height, prev_max, next_max, trapped_water) as (
select t.id, t.height, t.prev_max, t1.next_max,
       case when t.prev_max is null or t1.next_max is null then 0
            else greatest(0, least(t.prev_max, t1.next_max) - t.height)
       end as trapped_water
  from t
       inner join t1 on (t1.id = t.id)
-- order by t.id
)
select sum(trapped_water) as total_trapped_water
  from t2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Using hierarchical queries to determine prev_max and next_max
with recursive t (id, height, prev_max) as (
    select id, height, NULL::int as prev_max
      from heights
     where id = (select min(id) from heights)
   union all
   select h.id, h.height, greatest(t.height, coalesce(t.prev_max, 0))
     from t
          inner join heights h on (h.id = t.id + 1)
),
t1 (id, height, next_max) as (
    select id, height, NULL::int as next_max
      from heights
     where id = (select max(id) from heights)
    union all
    select h.id, h.height, greatest(t1.height, coalesce(t1.next_max, 0))
      from t1
           inner join heights h on (h.id = t1.id - 1)
),
t2 (id, height, prev_max, next_max, trapped_water) as (
select t.id, t.height, t.prev_max, t1.next_max,
       case when t.prev_max is null or t1.next_max is null then 0
            else greatest(0, least(t.prev_max, t1.next_max) - t.height)
       end as trapped_water
  from t
       inner join t1 on (t1.id = t.id)
-- order by t.id
)
select sum(trapped_water) as total_trapped_water
  from t2
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Using hierarchical queries to determine prev_max and next_max
with t (id, height, prev_max) as (
    select id, height, convert(int, NULL) as prev_max
      from heights
     where id = (select min(id) from heights)
   union all
   select h.id, h.height,
          case when t.height >= coalesce(t.prev_max, 0)
               then t.height
               else coalesce(t.prev_max, 0)
          end
     from t
          inner join heights h on (h.id = t.id + 1)
),
t1 (id, height, next_max) as (
    select id, height, convert(int, NULL) as next_max
      from heights
     where id = (select max(id) from heights)
    union all
    select h.id, h.height,
           case when t1.height >= coalesce(t1.next_max, 0)
                then t1.height
                else coalesce(t1.next_max, 0)
           end
      from t1
           inner join heights h on (h.id = t1.id - 1)
),
t2 (id, height, prev_max, next_max, trapped_water) as (
    select t.id, t.height, t.prev_max, t1.next_max,
           case when t.prev_max is null or t1.next_max is null
                then 0
                else
                     case when 0 >= case
                                        when t.prev_max <= t1.next_max
                                        then t.prev_max
                                        else t1.next_max
                                    end - t.height
                          then 0
                          else case
                                   when t.prev_max <= t1.next_max
                                   then t.prev_max
                                   else t1.next_max
                               end - t.height
                     end
           end as trapped_water
      from t
           inner join t1 on (t1.id = t.id)
    -- order by t.id
)
select sum(trapped_water) as total_trapped_water
  from t2
;


# MySQL
# Write your MySQL query statement below
# Using hierarchical queries to determine prev_max and next_max
with recursive t (id, height, prev_max) as (
    select id, height, -1 as prev_max
      from heights
     where id = (select min(id) from heights)
   union all
   select h.id, h.height, greatest(t.height, coalesce(t.prev_max, 0))
     from t
          inner join heights h on (h.id = t.id + 1)
),
t1 (id, height, next_max) as (
    select id, height, -1 as next_max
      from heights
     where id = (select max(id) from heights)
    union all
    select h.id, h.height, greatest(t1.height, coalesce(t1.next_max, 0))
      from t1
           inner join heights h on (h.id = t1.id - 1)
),
t2 (id, height, prev_max, next_max, trapped_water) as (
    select t.id, t.height, t.prev_max, t1.next_max,
           case when t.prev_max = -1 or t1.next_max = -1 then 0
                else greatest(0, least(t.prev_max, t1.next_max) - t.height)
           end as trapped_water
      from t
           inner join t1 on (t1.id = t.id)
)
select sum(trapped_water) as total_trapped_water
  from t2
;


# Pandas
import pandas as pd

def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    df_pre = ( heights
              .merge(heights, how='cross')
              .query('id_y < id_x')
              .groupby('id_x', as_index=0)['height_y'].max()
              .rename(columns={'id_x':'id','height_y':'pre_max_height'})
             )
    df_post = ( heights
               .merge(heights, how='cross')
               .query('id_y > id_x')
               .groupby('id_x', as_index=0)['height_y'].max()
               .rename(columns={'id_x':'id','height_y':'post_max_height'})
              )
    df = ( heights
          .merge(df_pre, how='left', on='id').fillna(0)
          .merge(df_post, how='left', on='id').fillna(0)
         )
    df['volume'] = df[['pre_max_height', 'post_max_height']].min(axis=1) - df['height']
    df['volume'] = np.where(
                     df.index==0, 0,
                                  np.where(
                                    df.index==len(df)-1, 0,
                                                         np.where(
                                                           df['volume']<0, 0, df['volume']
                                                         )
                                  )
                   )
    return pd.DataFrame(data={'total_trapped_water': df['volume'].sum()}, index=[0])

