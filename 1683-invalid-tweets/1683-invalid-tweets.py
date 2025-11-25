import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['con_len'] = tweets['content'].str.len()
    return pd.DataFrame(tweets[tweets['con_len']>15]['tweet_id'])