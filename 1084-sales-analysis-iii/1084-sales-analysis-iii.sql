# Write your MySQL query statement below
WITH TEMP AS(
    SELECT DISTINCT product_id as p_id
    FROM Sales
    WHERE sale_date between '2019-01-01' AND '2019-03-31'
        AND product_id NOT IN  (
            SELECT product_id
            FROM Sales
            WHERE sale_date > '2019-03-31' OR sale_date < '2019-01-01'
        )
    ORDER BY sale_date
)

SELECT product_id, product_name
FROM Product as p
    INNER JOIN TEMP as t ON p.product_id = t.p_id