# Write your MySQL query statement below
WITH TEMP AS(
    SELECT product_id, new_price as price
    FROM Products
    WHERE (product_id, change_date) IN (SELECT product_id, max(change_date)
                                        FROM Products as p
                                        WHERE change_date <= '2019-08-16'
                                        GROUP BY product_id)
)

SELECT product_id, price
FROM TEMP
UNION
SELECT product_id, 10 as price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM TEMP)
ORDER BY product_id asc