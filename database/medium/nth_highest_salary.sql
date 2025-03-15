-- Oracle
CREATE FUNCTION getNthHighestSalary(N IN NUMBER)
RETURN NUMBER
IS
    result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    with t (salary, drnk) as (
        select salary,
               dense_rank() over (order by salary desc) as drnk
          from (select distinct salary from employee)
    )
    select salary
      into result
      from t
     where drnk = N;
    RETURN result;
END;


-- PostgreSQL
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select y.salary
      from (select N as drnk) p
           left outer join (
               select distinct x.drnk, x.salary
                 from (
                         select e.salary,
                                dense_rank() over (order by e.salary desc) as drnk
                           from employee e
                      ) x
                where x.drnk = N
           ) y
           on (y.drnk = p.drnk)
  );
END;
$$ LANGUAGE plpgsql;


-- SQL Server
CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        select y.salary
          from (select @N as drnk) p
               left outer join (
                   select distinct x.drnk, x.salary
                     from (
                             select salary,
                                    dense_rank() over (order by salary desc) as drnk
                               from employee
                          ) x
                    where x.drnk = @N
               ) y
               on (y.drnk = p.drnk)
    );
END;


# MySQL
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select y.salary
        from (select N as drnk) p
             left outer join (
                 select distinct x.drnk, x.salary
                   from (
                           select e.salary,
                                  dense_rank() over (order by e.salary desc) as drnk
                             from employee e
                        ) x
                  where x.drnk = N
             ) y
             on (y.drnk = p.drnk)
  );
END


# Pandas
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    header = f'getNthHighestSalary({N})'
    employee['rank'] = employee.salary.rank(method='dense',ascending=False).astype('int')
    df = employee[employee['rank'] == N][['salary']]
    if len(df) == 0:
        return pd.DataFrame(data={header: [None]})
    df = df.drop_duplicates().rename(columns={'salary': header})
    return df

