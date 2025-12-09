import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees[['employee_id','name']].merge(employees[employees['reports_to'].notnull()][['reports_to','age']], left_on='employee_id', right_on='reports_to', how='right')

    result = result.groupby(['employee_id','name']).agg({'reports_to':'count','age':'mean'}).reset_index()
    result['age'] = round(result['age']+0.01,0)
    result.columns = ['employee_id','name','reports_count','average_age']
    return result