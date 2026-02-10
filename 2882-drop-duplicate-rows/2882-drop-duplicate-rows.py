import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    result = customers.iloc[customers['email'].drop_duplicates(keep='first').index,:]
    return result