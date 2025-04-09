-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_id, customer_name, contact, is_trusted) as (
select cst.customer_id, cst.customer_name,
       case when cnt.contact_name is null then 0 else 1 end as contact,
       case when cst1.email is null then 0 else 1 end as is_trusted
from customers cst
     left outer join contacts cnt on (cnt.user_id = cst.customer_id)
     left outer join customers cst1 on (cnt.contact_email = cst1.email)
)
,
t1 (customer_id, customer_name, contacts_cnt, trusted_contacts_cnt) as (
select customer_id, customer_name,
       sum(contact) as contacts_cnt,
       sum(is_trusted) as trusted_contacts_cnt
from t
group by customer_id, customer_name
)
select i.invoice_id, t1.customer_name, i.price, t1.contacts_cnt, t1.trusted_contacts_cnt
from invoices i
     inner join t1 on (t1.customer_id = i.user_id)
order by i.invoice_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (customer_id, customer_name, contact, is_trusted) as (
select cst.customer_id, cst.customer_name,
       case when cnt.contact_name is null then 0 else 1 end as contact,
       case when cst1.email is null then 0 else 1 end as is_trusted
from customers cst
     left outer join contacts cnt on (cnt.user_id = cst.customer_id)
     left outer join customers cst1 on (cnt.contact_email = cst1.email)
)
,
t1 (customer_id, customer_name, contacts_cnt, trusted_contacts_cnt) as (
select customer_id, customer_name,
       sum(contact) as contacts_cnt,
       sum(is_trusted) as trusted_contacts_cnt
from t
group by customer_id, customer_name
)
select i.invoice_id, t1.customer_name, i.price, t1.contacts_cnt, t1.trusted_contacts_cnt
from invoices i
     inner join t1 on (t1.customer_id = i.user_id)
order by i.invoice_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, customer_name, contact, is_trusted) as (
select cst.customer_id, cst.customer_name,
       case when cnt.contact_name is null then 0 else 1 end as contact,
       case when cst1.email is null then 0 else 1 end as is_trusted
from customers cst
     left outer join contacts cnt on (cnt.user_id = cst.customer_id)
     left outer join customers cst1 on (cnt.contact_email = cst1.email)
)
,
t1 (customer_id, customer_name, contacts_cnt, trusted_contacts_cnt) as (
select customer_id, customer_name,
       sum(contact) as contacts_cnt,
       sum(is_trusted) as trusted_contacts_cnt
from t
group by customer_id, customer_name
)
select i.invoice_id, t1.customer_name, i.price, t1.contacts_cnt, t1.trusted_contacts_cnt
from invoices i
     inner join t1 on (t1.customer_id = i.user_id)
order by i.invoice_id
;


# MySQL
# Write your MySQL query statement below
with t (customer_id, customer_name, contact, is_trusted) as (
select cst.customer_id, cst.customer_name,
       case when cnt.contact_name is null then 0 else 1 end as contact,
       case when cst1.email is null then 0 else 1 end as is_trusted
from customers cst
     left outer join contacts cnt on (cnt.user_id = cst.customer_id)
     left outer join customers cst1 on (cnt.contact_email = cst1.email)
)
,
t1 (customer_id, customer_name, contacts_cnt, trusted_contacts_cnt) as (
select customer_id, customer_name,
       sum(contact) as contacts_cnt,
       sum(is_trusted) as trusted_contacts_cnt
from t
group by customer_id, customer_name
)
select i.invoice_id, t1.customer_name, i.price, t1.contacts_cnt, t1.trusted_contacts_cnt
from invoices i
     inner join t1 on (t1.customer_id = i.user_id)
order by i.invoice_id
;


# Pandas
import pandas as pd

def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:
    df = (  customers.merge(contacts,
                                how='left',
                                left_on='customer_id',
                                right_on='user_id'
                           )[['customer_id','customer_name','contact_name']]
         )
    df1 = (  contacts.merge(customers,
                                how='left',
                                left_on='contact_email',
                                right_on='email'
                           )[['contact_name','email']]
                     .drop_duplicates()
          )
    df1['email'] = np.where(df1['email'].isna(),0,1)
    df2 = (  df.merge(df1, how='left', on='contact_name')
               .groupby(['customer_id','customer_name'],as_index=False)
               .agg(contacts_cnt=('contact_name','count'), trusted_contacts_cnt=('email','sum'))
          )
    return (  invoices.merge(df2,
                               how='inner',
                               left_on='user_id',
                               right_on='customer_id'
                            )[['invoice_id','customer_name','price','contacts_cnt','trusted_contacts_cnt']]
                      .sort_values('invoice_id')
           )

