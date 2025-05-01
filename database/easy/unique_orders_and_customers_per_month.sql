-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = orders['order_date'].dt.strftime('%Y-%m')
    return (  orders[orders['invoice'] > 20]
              .groupby('order_date',as_index=False)[['order_id','customer_id']]
              .nunique()
              .rename(columns={'order_date':'month', 'order_id':'order_count', 'customer_id':'customer_count'})
           )

