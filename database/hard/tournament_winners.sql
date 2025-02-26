-- Oracle
/* Write your PL/SQL query statement below */
with t (player_id, score) as (
    select first_player, first_score
      from matches
    union all
    select second_player, second_score
      from matches
),
t1 (group_id, player_id, total_score) as (
    select p.group_id, t.player_id, sum(t.score) as total_score
      from players p
           inner join t on (t.player_id = p.player_id)
     group by p.group_id, t.player_id
),
t2 (group_id, player_id, total_score, drnk) as (
    select group_id, player_id, total_score,
           dense_rank() over (partition by group_id order by total_score desc, player_id) as drnk
      from t1
)
select group_id, player_id
  from t2
 where drnk = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (player_id, score) as (
    select first_player, first_score
      from matches
    union all
    select second_player, second_score
      from matches
),
t1 (group_id, player_id, total_score) as (
    select p.group_id, t.player_id, sum(t.score) as total_score
      from players p
           inner join t on (t.player_id = p.player_id)
     group by p.group_id, t.player_id
),
t2 (group_id, player_id, total_score, drnk) as (
    select group_id, player_id, total_score,
           dense_rank() over (partition by group_id order by total_score desc, player_id) as drnk
      from t1
)
select group_id, player_id
  from t2
 where drnk = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (player_id, score) as (
    select first_player, first_score
      from matches
    union all
    select second_player, second_score
      from matches
),
t1 (group_id, player_id, total_score) as (
    select p.group_id, t.player_id, sum(t.score) as total_score
      from players p
           inner join t on (t.player_id = p.player_id)
     group by p.group_id, t.player_id
),
t2 (group_id, player_id, total_score, drnk) as (
    select group_id, player_id, total_score,
           dense_rank() over (partition by group_id order by total_score desc, player_id) as drnk
      from t1
)
select group_id, player_id
  from t2
 where drnk = 1
;


# MySQL
# Write your MySQL query statement below
with t (player_id, score) as (
    select first_player, first_score
      from matches
    union all
    select second_player, second_score
      from matches
),
t1 (group_id, player_id, total_score) as (
    select p.group_id, t.player_id, sum(t.score) as total_score
      from players p
           inner join t on (t.player_id = p.player_id)
     group by p.group_id, t.player_id
),
t2 (group_id, player_id, total_score, drnk) as (
    select group_id, player_id, total_score,
           dense_rank() over (partition by group_id order by total_score desc, player_id) as drnk
      from t1
)
select group_id, player_id
  from t2
 where drnk = 1
;


# Pandas
import pandas as pd

def tournament_winners(players: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([
        matches[['first_player','first_score']].rename(columns={'first_player':'player_id','first_score':'score'}),
        matches[['second_player','second_score']].rename(columns={'second_player':'player_id','second_score':'score'})
    ])
    df1 = ( df
           .merge(players, how='inner', on='player_id')
           .groupby(['group_id','player_id'], as_index=0)['score']
           .sum()
          )
    return ( df1
            .assign(drnk=df1.groupby('group_id', as_index=0)['score'].rank(method='dense', ascending=False))
            .query('drnk==1')
            .groupby('group_id', as_index=0)['player_id']
            .min()
           )

