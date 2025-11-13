# Write your MySQL query statement below
WITH tmp AS(
SELECT a1.machine_id, a1.process_id, a1.start_time, a2.end_time
FROM (SELECT machine_id, process_id, (timestamp) as start_time
          FROM Activity
          WHERE activity_type = 'start') as a1
    JOIN (SELECT machine_id, process_id, (timestamp) as end_time
          FROM Activity
          WHERE activity_type = 'end') as a2 ON (a1.machine_id = a2.machine_id) AND (a1.process_id = a2.process_id)
)
SELECT machine_id, round(avg(end_time - start_time),3) as processing_time
FROM tmp
GROUP BY machine_id