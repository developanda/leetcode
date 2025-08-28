import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values(by='turn')
    queue['cum_weight'] = queue['weight'].cumsum()
    queue = queue[queue['cum_weight']<=1000]
    result = pd.DataFrame(queue.iloc[-1, :]['person_name'])

    return result