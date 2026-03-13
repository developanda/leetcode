import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:

            # We sort scores by student_id, subject, and exam_date
    df = scores.sort_values(['student_id', 'subject', 'exam_date'])

            # We use groupby and agg to filter for first and latest scores
    df = (df.groupby(['student_id', 'subject'])['score'].agg(
                first_score = 'first', 
               latest_score = 'last')
            .reset_index())

            # We filter for the improvement criterion
    return df[df.latest_score > df.first_score]