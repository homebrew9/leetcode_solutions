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

