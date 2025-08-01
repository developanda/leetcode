import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.drop_duplicates()
    
    result = actor_director.groupby(by=['actor_id','director_id'])['timestamp'].count().reset_index()
    return result[result['timestamp']>=3][['actor_id','director_id']]