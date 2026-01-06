import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    result = logins[(logins['time_stamp']>='2020-01-01')&(logins['time_stamp']<'2021-01-01')].groupby('user_id')['time_stamp'].max().reset_index()
    result.columns = ['user_id', 'last_stamp']
    return result