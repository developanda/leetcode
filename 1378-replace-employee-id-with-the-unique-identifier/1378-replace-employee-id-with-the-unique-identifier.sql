# Write your MySQL query statement below
SELECT eu.unique_id, es.name
FROM Employees as es
    LEFT JOIN EmployeeUNI as eu ON es.id = eu.id