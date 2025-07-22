# Write your MySQL query statement below
WITH TEMP AS (
    SELECT num, count(num) as cnt
    FROM MyNumbers
    GROUP BY num
    HAVING count(num) < 2
)

SELECT max(num) as num
FROM TEMP