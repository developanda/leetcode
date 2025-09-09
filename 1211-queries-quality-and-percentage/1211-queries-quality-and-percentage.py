import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.copy()
    df['quality_ratio'] = df.rating/df.position + 1e-6
    df['poor_query'] = df.apply(lambda row: 100 if row.rating < 3 else 0, axis =1)
    df_output = df.groupby(by='query_name').agg(
        quality = ('quality_ratio', 'mean'),
        poor_query_percentage = ('poor_query', 'mean')
        # queries = ('rating', 'size')
    ).reset_index()
    

    return df_output[['query_name','quality', 'poor_query_percentage']].round(2)