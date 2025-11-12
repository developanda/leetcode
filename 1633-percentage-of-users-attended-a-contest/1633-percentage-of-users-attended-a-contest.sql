# Write your MySQL query statement below
SELECT contest_id, round(count(r.user_id)/(SELECT count(*)
                                            FROM Users),4)*100 as percentage
FROM Register as r 
GROUP BY contest_id
ORDER BY percentage desc, contest_id asc