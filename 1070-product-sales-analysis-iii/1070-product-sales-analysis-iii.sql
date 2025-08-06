# Write your MySQL query statement below
WITH TEMP AS(
    SELECT DISTINCT product_id as id, min(year) as first_year
    FROM Sales
    GROUP BY product_id
)

SELECT product_id, year as first_year, quantity, price
FROM Sales 
    JOIN TEMP ON (Sales.product_id = TEMP.id) AND (Sales.year = TEMP.first_year)