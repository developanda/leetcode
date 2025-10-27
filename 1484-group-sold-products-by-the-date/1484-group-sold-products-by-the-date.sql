# Write your MySQL query statement below
WITH TEMP AS (
    SELECT DISTINCT *
    FROM Activities
)

SELECT DISTINCT sell_date
       ,  count(product) as num_sold
       , GROUP_CONCAT(product order by product, ',') as products
FROM TEMP
GROUP BY sell_date
ORDER BY sell_date, num_sold