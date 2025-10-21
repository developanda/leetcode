# Write your MySQL query statement below
SELECT u.name, coalesce(r.sum_distance,0) as travelled_distance 
FROM Users as u 
    LEFT JOIN (SELECT user_id, sum(distance) as sum_distance
               FROM Rides
               GROUP BY user_id) as r ON u.id = r.user_id
ORDER BY r.sum_distance desc, u.name asc