# Write your MySQL query statement below
# 1. first test date, last test date, date by student, subject
WITH rank_date AS(
    SELECT student_id, subject, row_number() over (partition by student_id, subject order by exam_date ASC) as first_date, row_number() over (partition by student_id, subject order by exam_date DESC) as last_date, score
    FROM Scores
)

# 2. merge data, second subject score, date by student
SELECT f.student_id, f.subject, (f.score) as first_score, (l.score) as latest_score
FROM rank_date as f
    JOIN rank_date as l ON (f.student_id = l.student_id) AND (f.subject = l.subject)
WHERE (f.first_date = 1) AND (l.last_date = 1) AND (f.first_date != f.last_date) AND (f.score < l.score)