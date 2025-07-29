import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    result = salary.replace({'sex':{'m':'f', 'f':'m'}})
    return result