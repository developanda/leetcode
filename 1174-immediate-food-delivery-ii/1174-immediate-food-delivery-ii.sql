# Write your MySQL query statement below
WITH TEMP AS (
    SELECT customer_id , order_date as first_date, DATEDIFF(customer_pref_delivery_date, order_date) as immediate_delivery
    FROM Delivery
    GROUP BY customer_id, immediate_delivery
    ORDER BY customer_id, order_date, customer_pref_delivery_date 
)

SELECT ROUND(SUM(immediate_delivery)/COUNT(immediate_delivery), 4) * 100 as immediate_percentage
FROM (SELECT customer_id, min(first_date) as min_date, IF(immediate_delivery > 0, 0, 1) as immediate_delivery
      FROM TEMP
      GROUP BY customer_id) as f_table