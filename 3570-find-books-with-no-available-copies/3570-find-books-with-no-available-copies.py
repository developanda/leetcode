import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    borrow_df = borrowing_records[borrowing_records['return_date'].isnull()].groupby('book_id')['record_id'].count().reset_index()

    result = library_books.merge(borrow_df, on = 'book_id', how='left')
    result['remain'] = result['total_copies'] - result['record_id']

    result = result[result['remain']==0].sort_values(['record_id','title'], ascending=[False, True])
    result = result.rename(columns={'record_id':'current_borrowers'})
    return result[['book_id','title','author','genre','publication_year','current_borrowers']]