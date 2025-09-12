# Write your MySQL query statement below
SELECT s.student_id, s.student_name, s.subject_name, coalesce(e.attended_exames,0) as attended_exames
FROM (SELECT *
      FROM Students
          CROSS JOIN Subjects) as s
    LEFT JOIN (SELECT student_id, subject_name, count(subject_name) as attended_exams 
               FROM Examinations
               GROUP BY student_id, subject_name) as e 
    ON (s.student_id = e.student_id) AND ((s.subject_name = e.subject_name))
ORDER BY s.student_id, s.student_name, s.subject_name, e.attended_exames