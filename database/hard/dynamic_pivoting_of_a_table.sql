-- Oracle
CREATE FUNCTION PivotProducts
RETURN SYS_REFCURSOR
IS
    result SYS_REFCURSOR;
    v_column_list varchar2(4000);
    v_sql         varchar2(4000);
BEGIN
    /* Write your PL/SQL query statement below */
    select listagg(''''||p.store||''' as "'||p.store||'"', ', ') within group (order by p.store)
      into v_column_list
      from (select distinct store from products) p;
    v_sql := 'select * from products pivot (max(price) for store in ( '||v_column_list||' ))';
    OPEN result for v_sql;    
    RETURN result;
END;


-- PostgreSQL


-- SQL Server
CREATE PROCEDURE PivotProducts AS
BEGIN
    /* Write your T-SQL query statement below. */
    DECLARE @v_columns nvarchar(max),
            @v_sql nvarchar(max);
    select @v_columns=STRING_AGG('max(case when store = '''+x.store+''' then price end) as ['+x.store+']', ', ')
      from (select distinct store from dbo.products) x;
    SET @v_sql = 'select product_id, '+ @v_columns +' from dbo.products group by product_id';
    EXEC sp_executesql @v_sql;
END


# MySQL
CREATE PROCEDURE PivotProducts()
BEGIN
	# Write your MySQL query statement below.
    # The default max length of group_concat() function output is 1024.
    SET SESSION group_concat_max_len = 1000000;
    SET @v_columns := (
        select group_concat(
                   CONCAT('sum(case when store = ''', x.store, ''' then price end) as "', x.store, '"')
                   order by x.store separator ', '
               )
          from (select distinct store from products) x
    );
    SET @sql_statement := CONCAT('select product_id, ', @v_columns, ' from products group by product_id');
    PREPARE dynamic_statement FROM @sql_statement;
    EXECUTE dynamic_statement;
END


# Pandas
import pandas as pd

def dynamic_pivoting_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(products, index='product_id', columns='store', values='price', aggfunc='max').reset_index()

