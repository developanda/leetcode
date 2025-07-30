# Write your MySQL query statement below
SELECT customer_id
FROM Customer as c
    RIGHT JOIN Product as p ON c.product_key = p.product_key
WHERE c.product_key IS NOT NULL
GROUP BY c.customer_id
HAVING count(c.customer_id)>1