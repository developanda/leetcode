# Write your MySQL query statement below
WITH tmp as(
    SELECT p.product_id, p.product_name, sum(o.unit) as unit
    FROM Products as p
        JOIN Orders as o ON p.product_id = o.product_id
    WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY p.product_id, p.product_name
)
SELECT product_name, unit
FROM tmp
WHERE unit >= 100