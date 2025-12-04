# Write your MySQL query statement below
SELECT e1.employee_id, name, count(e2.reports_to) as reports_count, round(avg(e2.age),0) as average_age
FROM Employees as e1 
    INNER JOIN (SELECT reports_to, age 
                FROM Employees ) as e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, name
ORDER BY e1.employee_id