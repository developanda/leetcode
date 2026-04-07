import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    return (
    employees
    .merge(performance_reviews, on='employee_id', how='left')
    .sort_values( by = ['employee_id', 'review_date'], ascending = [True, False]) 
    .assign(
        review_count=lambda x: x.groupby('employee_id')['review_id'].transform('count')
        ,rnk=lambda x: x.groupby('name').cumcount() + 1
    )
    .query("(review_count >= 3) & (rnk <= 3)")
    .assign(
        lead = lambda x: x.groupby('employee_id')['rating'].shift(-1)
        ,lag  = lambda x: x.groupby('employee_id')['rating'].shift(-2)
        ,improvement_score = lambda row : row['rating'] - row['lag']
    )
    .query("(rating.notna()) & (lead.notna())")
    .query("(rating > lead)  & (lead > lag)")[['employee_id', 'name', 'improvement_score']]
    .drop_duplicates(subset = ['employee_id', 'name'], keep  = 'first')
    .sort_values(by = ['improvement_score', 'name'], ascending = [False, True])
    )