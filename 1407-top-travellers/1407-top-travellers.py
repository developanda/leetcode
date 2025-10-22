import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df=rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    df=users.merge(df, left_on='id', right_on='user_id', how='left')
    df['travelled_distance'] = df['travelled_distance'].fillna(0)
    return df[['name','travelled_distance']].sort_values(['travelled_distance','name'], ascending=[False, True])