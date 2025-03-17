-- Oracle
/* Important: For this problem, column names are case sensitive.
              You should use double quotes while using the columns.
 */

CREATE FUNCTION UnpivotProducts
RETURN SYS_REFCURSOR
IS
    result SYS_REFCURSOR;
    v_unpivot_list  varchar2(32767);
    v_sql varchar2(32767);
BEGIN
    /* Write your PL/SQL query statement below */
    select listagg('"'||column_name||'"', ',') within group (order by column_name)
    into v_unpivot_list
    from all_tab_columns
    where upper(table_name) = 'PRODUCTS'
    and upper(column_name) <> 'PRODUCT_ID';

    v_sql := 'select * from products unpivot (price for store in ( ' || v_unpivot_list || '))';
    OPEN result FOR v_sql;
    RETURN result;
END;


-- PostgreSQL
-- There is no option for PostgreSQL in the drop-down.


-- SQL Server
CREATE PROCEDURE UnpivotProducts AS
BEGIN
    /* Write your T-SQL query statement below. */
    DECLARE @v_sql nvarchar(max),
            @v_store_list nvarchar(max);
    SET @v_store_list = (select string_agg('['+name+']', ',') as col_list
                           from sys.columns
                          where object_name(object_id) = 'products'
                            and name != 'product_id'
                        );
    SET @v_sql = N'select product_id, store, price from products p unpivot (price for store in (' + @v_store_list + ')) unpvt';
    EXEC sp_executesql @v_sql;
END


# MySQL
CREATE PROCEDURE UnpivotProducts()
BEGIN
	# Write your MySQL query statement below.
    set session group_concat_max_len = 1000000;
    SET @cols_list = (
        select GROUP_CONCAT(concat('select ',column_name, ', ''', column_name, '''') SEPARATOR ' UNION ALL ') as x
          from information_schema.columns
         where table_name = 'products'
           and column_name != 'product_id'
    );
    
    SET @s = CONCAT('select p.product_id, x.store, x.price
                       from products p
                            cross join lateral (',
                                @cols_list,
                            ') as x (price, store)
                      where x.price is not null'
                   );
    PREPARE stmt FROM @s;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END


# Pandas
import pandas as pd

def find_valid_users(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars='product_id', var_name='store', value_name='price').query('~price.isnull()')

