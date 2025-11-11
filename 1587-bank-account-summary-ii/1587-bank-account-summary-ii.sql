# Write your MySQL query statement below
WITH TMP AS (
SELECT u.name as name, sum(amount) as balance
FROM Transactions as t
    LEFT JOIN Users as u ON t.account = u.account
GROUP BY u.name
)
SELECT name, balance
FROM TMP
WHERE balance > 10000