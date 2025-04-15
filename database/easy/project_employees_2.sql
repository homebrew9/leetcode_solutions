-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.groupby('project_id', as_index=False)['employee_id'].count()
    return df[df['employee_id'] == df['employee_id'].max()][['project_id']]

