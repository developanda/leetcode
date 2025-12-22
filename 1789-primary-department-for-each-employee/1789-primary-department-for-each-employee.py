import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    tmp = employee.groupby('employee_id')['department_id'].count().reset_index()
    tmp.columns = ['employee_id','cnt_emp']

    result = employee.merge(tmp, on='employee_id', how='left')
    result = result[(result['primary_flag']=='Y')|(result['cnt_emp']==1)]

    return result[['employee_id', 'department_id']]