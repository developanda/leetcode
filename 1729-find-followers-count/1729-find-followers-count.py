import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = followers.groupby('user_id')['follower_id'].nunique().reset_index()
    
    result.sort_values('user_id', inplace=True)
    result.columns = ['user_id', 'followers_count']
    return result
