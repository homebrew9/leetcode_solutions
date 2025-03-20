-- Oracle
/* Write your PL/SQL query statement below */
with project_candidate (project_id, candidate_id) as (
    select p.project_id, c.candidate_id
      from (select distinct project_id
              from projects
           ) p
           cross join (select distinct candidate_id
                         from candidates
                      ) c
),
proj_cand as (
    select project_id, candidate_id
      from project_candidate pc
     where not exists ( select null
                          from projects x
                         where x.project_id = pc.project_id
                           and x.skill not in ( select y.skill
                                                  from candidates y
                                                 where y.candidate_id = pc.candidate_id
                                              )
                      )
),
t as (
    select p.project_id, c.candidate_id,
           100 + sum(case when c.proficiency > p.importance then 10
                          when c.proficiency < p.importance then -5
                          else 0
                     end
                    ) as score
      from proj_cand pc
           inner join projects p on (p.project_id = pc.project_id)
           inner join candidates c on (c.candidate_id = pc.candidate_id and c.skill = p.skill)
     group by p.project_id, c.candidate_id
),
t1 as (
    select project_id, candidate_id, score,
           dense_rank() over (partition by project_id order by score desc, candidate_id) as drnk
      from t
)
select project_id, candidate_id, score
  from t1
 where drnk = 1
 order by project_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with project_candidate (project_id, candidate_id) as (
    select p.project_id, c.candidate_id
      from (select distinct project_id
              from projects
           ) p
           cross join (select distinct candidate_id
                         from candidates
                      ) c
),
proj_cand as (
    select project_id, candidate_id
      from project_candidate pc
     where not exists ( select null
                          from projects x
                         where x.project_id = pc.project_id
                           and x.skill not in ( select y.skill
                                                  from candidates y
                                                 where y.candidate_id = pc.candidate_id
                                              )
                      )
),
t as (
    select p.project_id, c.candidate_id,
           100 + sum(case when c.proficiency > p.importance then 10
                          when c.proficiency < p.importance then -5
                          else 0
                     end
                    ) as score
      from proj_cand pc
           inner join projects p on (p.project_id = pc.project_id)
           inner join candidates c on (c.candidate_id = pc.candidate_id and c.skill = p.skill)
     group by p.project_id, c.candidate_id
),
t1 as (
    select project_id, candidate_id, score,
           dense_rank() over (partition by project_id order by score desc, candidate_id) as drnk
      from t
)
select project_id, candidate_id, score
  from t1
 where drnk = 1
 order by project_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with project_candidate (project_id, candidate_id) as (
    select p.project_id, c.candidate_id
      from (select distinct project_id
              from projects
           ) p
           cross join (select distinct candidate_id
                         from candidates
                      ) c
),
proj_cand as (
    select project_id, candidate_id
      from project_candidate pc
     where not exists ( select null
                          from projects x
                         where x.project_id = pc.project_id
                           and x.skill not in ( select y.skill
                                                  from candidates y
                                                 where y.candidate_id = pc.candidate_id
                                              )
                      )
),
t as (
    select p.project_id, c.candidate_id,
           100 + sum(case when c.proficiency > p.importance then 10
                          when c.proficiency < p.importance then -5
                          else 0
                     end
                    ) as score
      from proj_cand pc
           inner join projects p on (p.project_id = pc.project_id)
           inner join candidates c on (c.candidate_id = pc.candidate_id and c.skill = p.skill)
     group by p.project_id, c.candidate_id
),
t1 as (
    select project_id, candidate_id, score,
           dense_rank() over (partition by project_id order by score desc, candidate_id) as drnk
      from t
)
select project_id, candidate_id, score
  from t1
 where drnk = 1
 order by project_id
;


# MySQL
# Write your MySQL query statement below
with project_candidate (project_id, candidate_id) as (
    select p.project_id, c.candidate_id
      from (select distinct project_id
              from projects
           ) p
           cross join (select distinct candidate_id
                         from candidates
                      ) c
),
proj_cand as (
    select project_id, candidate_id
      from project_candidate pc
     where not exists ( select null
                          from projects x
                         where x.project_id = pc.project_id
                           and x.skill not in ( select y.skill
                                                  from candidates y
                                                 where y.candidate_id = pc.candidate_id
                                              )
                      )
),
t as (
    select p.project_id, c.candidate_id,
           100 + sum(case when c.proficiency > p.importance then 10
                          when c.proficiency < p.importance then -5
                          else 0
                     end
                    ) as score
      from proj_cand pc
           inner join projects p on (p.project_id = pc.project_id)
           inner join candidates c on (c.candidate_id = pc.candidate_id and c.skill = p.skill)
     group by p.project_id, c.candidate_id
),
t1 as (
    select project_id, candidate_id, score,
           dense_rank() over (partition by project_id order by score desc, candidate_id) as drnk
      from t
)
select project_id, candidate_id, score
  from t1
 where drnk = 1
 order by project_id
;


# Pandas
import pandas as pd

def find_best_candidates(candidates: pd.DataFrame, projects: pd.DataFrame) -> pd.DataFrame:
    # Cross join projects with all distinct candidates, and then left join with candidates
    # on candidate_id and skill.
    df = ( projects
          .merge(candidates[['candidate_id']].drop_duplicates(), how='cross')
          .merge(candidates, how='left', on=['candidate_id','skill'])
         )
    
    # If a candidate proficiency is NULL, then that candidate does not have all skills for
    # the project. We need to remove all such (project_id, candidate_id) tuples.
    df1 = df[df['proficiency'].isna()][['project_id','candidate_id']]
    
    # A hack to compare .isin() with multiple columns!
    df1['indicator'] = df1['project_id'].astype(str) + '#' + df1['candidate_id'].astype(str)
    df = df[~(df['project_id'].astype(str)+'#'+df['candidate_id'].astype(str)).isin(df1['indicator'])]
    
    # Now assign the score for all suitable candidates
    df['score'] = np.where(df['proficiency'] > df['importance'], 10, np.where(df['proficiency'] < df['importance'], -5, 0))
    df = df.groupby(['project_id','candidate_id'], as_index=0)['score'].sum()
    df['score'] = df['score'] + 100
    
    # Rank by highest to lowest score and for each such rank, do further ranking on candidate_id ascending
    df['srnk'] = df.groupby('project_id', as_index=0)['score'].rank(method='dense', ascending=False)
    return ( df
            .assign(crnk=df.groupby(['project_id','srnk'], as_index=0)['candidate_id'].rank(method='dense', ascending=True))
            .query('srnk == 1 & crnk == 1')[['project_id','candidate_id','score']]
            .sort_values('project_id')
           )

