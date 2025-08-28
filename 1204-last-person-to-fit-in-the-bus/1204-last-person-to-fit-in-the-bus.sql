# Write your MySQL query statement below
WITH TEMP AS (
SELECT *, sum(weight) over(order by turn) as cum_weight
FROM Queue
)

SELECT person_name
FROM TEMP
WHERE (turn = (SELECT max(turn) FROM TEMP WHERE cum_weight <= 1000))
