# Write your MySQL query statement below
WITH tmp AS(
    SELECT s.user_id, s.time_stamp, CASE WHEN c.action='timeout' THEN 0
                                          WHEN c.action='confirmed' THEN 1
                                          ELSE 0
                                     END AS confirmation
    FROM Signups as s
        LEFT JOIN Confirmations as c ON s.user_id = c.user_id
)
SELECT user_id, sum(confirmation)/count(confirmation) as confirmation_rate
FROM tmp
GROUP BY user_id