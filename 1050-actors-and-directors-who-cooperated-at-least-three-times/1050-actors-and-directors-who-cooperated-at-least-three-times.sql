# Write your MySQL query statement below
WITH Temp as (
    SELECT actor_id,director_id, count(timestamp) as cooperated
    FROM ActorDirector
    GROUP BY actor_id, director_id
    Having cooperated>=3
)

SELECT actor_id, director_id
FROM Temp
