-- Oracle
/* Write your PL/SQL query statement below */
select a.player_id, a.device_id
  from activity a
 where a.event_date = (select min(a1.event_date)
                         from activity a1
                        where a1.player_id = a.player_id
                      )
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

