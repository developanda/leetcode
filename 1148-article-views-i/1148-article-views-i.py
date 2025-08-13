import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views['author_id']==views['viewer_id']]
    result = result.sort_values('author_id').rename(columns={'author_id':'id'})['id']
    return pd.DataFrame(result.drop_duplicates(keep='first'))