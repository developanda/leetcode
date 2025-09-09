import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating']/queries['position']

    queries['poor_query_percentage'] = 0
    queries.loc[queries['rating'] < 3, 'poor_query_percentage'] = 100


    result = queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().reset_index()
    result['quality'] = round(result['quality'],2)
    result['poor_query_percentage'] = round(result['poor_query_percentage'],2)
    return result