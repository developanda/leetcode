import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    user_activity['activity_type2'] = user_activity['activity_type'].shift(1)
    user_activity['user_id2'] = user_activity['user_id'].shift(1)

    paid_user_lst = list(user_activity[(user_activity['activity_type']=='paid')&(user_activity['activity_type2']=='free_trial')&(user_activity['user_id']==user_activity['user_id2'])]['user_id'])

    select_df = user_activity[user_activity['user_id'].isin(paid_user_lst)]

    result = select_df.groupby(['user_id','activity_type'])['activity_duration'].mean().reset_index()
    result2 = result[result['activity_type']!='cancelled'].pivot_table(index='user_id', columns='activity_type', values='activity_duration').reset_index()
    result2.rename(columns={'free_trial':'trial_avg_duration', 'paid':'paid_avg_duration'}, inplace=True)
    result2[['trial_avg_duration','paid_avg_duration']] = round(result2[['trial_avg_duration','paid_avg_duration']]+0.0001,2)

    return result2