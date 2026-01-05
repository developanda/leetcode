# Write your MySQL query statement below
SELECT user_id, max(time_stamp) as last_stamp
FROM Logins
WHERE  (time_stamp >= '2020-01-01 00:00:00') 
       AND (time_stamp < '2021-01-01 00:00:00') 
       AND (user_id in (SELECT DISTINCT(user_id)
                        FROM Logins
                        WHERE (time_stamp >= '2020-01-01 00:00:00') AND (time_stamp < '2021-01-01 00:00:00')))
GROUP BY user_id