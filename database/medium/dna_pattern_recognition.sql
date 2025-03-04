-- Oracle
/* Write your PL/SQL query statement below */
select sample_id, dna_sequence, species,
       case when substr(dna_sequence, 1, 3) = 'ATG' then 1 else 0 end as has_start,
       case when substr(dna_sequence, length(dna_sequence)-2) in ('TAA','TAG','TGA') then 1 else 0 end as has_stop, 
       case when instr(dna_sequence, 'ATAT') <> 0 then 1 else 0 end as has_atat,
       case when instr(dna_sequence, 'GGG') <> 0 then 1 else 0 end as has_ggg
  from samples
 order by sample_id
 ;
 

-- PostgreSQL
-- Write your PostgreSQL query statement below
select sample_id, dna_sequence, species,
       case when left(dna_sequence, 3) = 'ATG' then 1 else 0 end as has_start,
       case when right(dna_sequence, 3) in ('TAA','TAG','TGA') then 1 else 0 end as has_stop, 
       case when strpos(dna_sequence, 'ATAT') <> 0 then 1 else 0 end as has_atat,
       case when strpos(dna_sequence, 'GGG') <> 0 then 1 else 0 end as has_ggg
  from samples
 order by sample_id
 ;
 

-- SQL Server
/* Write your T-SQL query statement below */
select sample_id, dna_sequence, species,
       case when left(dna_sequence, 3) = 'ATG' then 1 else 0 end as has_start,
       case when right(dna_sequence, 3) in ('TAA','TAG','TGA') then 1 else 0 end as has_stop, 
       case when charindex('ATAT', dna_sequence) <> 0 then 1 else 0 end as has_atat,
       case when charindex('GGG', dna_sequence) <> 0 then 1 else 0 end as has_ggg
  from samples
 order by sample_id
 ;
 

# MySQL
# Write your MySQL query statement below
select sample_id, dna_sequence, species,
       case when substr(dna_sequence, 1, 3) = 'ATG' then 1 else 0 end as has_start,
       case when substr(dna_sequence, length(dna_sequence)-2) in ('TAA','TAG','TGA') then 1 else 0 end as has_stop, 
       case when instr(dna_sequence, 'ATAT') <> 0 then 1 else 0 end as has_atat,
       case when instr(dna_sequence, 'GGG') <> 0 then 1 else 0 end as has_ggg
  from samples
 order by sample_id
 ;
 

# Pandas
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = np.where(samples['dna_sequence'].str[:3]=='ATG', 1, 0)
    samples['has_stop'] = np.where(samples['dna_sequence'].str[-3:].isin(['TAA','TAG','TGA']), 1, 0)
    samples['has_atat'] = np.where(samples['dna_sequence'].str.contains('ATAT'), 1, 0)
    samples['has_ggg'] = np.where(samples['dna_sequence'].str.contains('GGG'), 1, 0)
    return samples.sort_values('sample_id')

