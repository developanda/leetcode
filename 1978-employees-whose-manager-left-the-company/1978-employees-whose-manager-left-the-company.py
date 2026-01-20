import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    con_data1 = employees[~(employees['manager_id'].isin(list(employees['employee_id'].unique())))]
    con_data2 = con_data1[(con_data1['salary']<30000)&(~con_data1['manager_id'].isnull())].sort_values('employee_id')

    result = pd.DataFrame(con_data2['employee_id'])
    return result