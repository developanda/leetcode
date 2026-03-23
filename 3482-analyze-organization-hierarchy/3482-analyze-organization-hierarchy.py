import pandas as pd

def f(x):
    rslt = []
    for k in x: rslt += list(k)
    return rslt

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    employees[['level', 'team_size', 'budget']] = [1,0,0]
    employees['sub'] = employees.apply(lambda _: [], axis=1)
    df = employees.groupby('manager_id').agg(sub=('employee_id', 'unique'))
    employees.set_index('employee_id', inplace=True)
    employees.update(df)

    idx = employees.index[employees['sub'].apply(lambda x: len(x) == 0)]
    while idx.size:
        employees.loc[idx, 'budget'] = employees.loc[idx,'salary'] + employees.loc[idx, 'sub'].apply(lambda x: employees.loc[x, 'budget'].sum())
        employees.loc[idx, 'team_size'] = employees.loc[idx, 'sub'].apply(lambda x: len(x) + employees.loc[x, 'team_size'].sum())
        idx = pd.Index(employees.loc[idx, 'manager_id'].unique()).dropna()

    t = f(employees[employees['manager_id'].isna()]['sub'].values.tolist())
    current_level = 2
    while t:
        employees.loc[t, 'level'] = current_level
        current_level += 1
        t = f(employees.loc[t, 'sub'].values.tolist())
    
    return (employees
             .drop(columns=['sub', 'manager_id', 'salary', 'department'])
             .reset_index()
             .sort_values(by=['level', 'budget'], ascending=[1,0]))
    
    boss = df.loc[df.manager_id.isna(), "employee_id"].values[0]
    
    for mgr, emp, sal in zip(df.manager_id, df.employee_id, df.salary):
        grph[mgr].append(emp)
        bdgt[emp] = sal   
    
    traverseGraph(boss,1)

    df['level']     = df.employee_id.apply(lambda x: levl[x])
    df['team_size'] = df.employee_id.apply(lambda x: team[x])
    df['budget']    = df.employee_id.apply(lambda x: bdgt[x])

    return df.sort_values(['level','budget','employee_name'], 
                        ascending  = [1,0,1]).iloc[:,[0,1, 5, 6, 7]]