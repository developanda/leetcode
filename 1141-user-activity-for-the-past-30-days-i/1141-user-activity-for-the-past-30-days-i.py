import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    temp = activity[(activity['activity_date']<='2019-07-27')&(activity['activity_date']>'2019-06-27')]

    result = temp.groupby('activity_date')['user_id'].nunique().reset_index()
    result.columns = ['day', 'active_users']
    return result