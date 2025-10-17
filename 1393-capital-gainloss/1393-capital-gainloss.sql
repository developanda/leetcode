# Write your MySQL query statement below
WITH TEMP as (
    SELECT *, (CASE operation 
                WHEN 'Buy' THEN -1
                ELSE 1
               END) as by_p
    FROM Stocks
)
SELECT stock_name, sum(price*by_p)as capital_gain_loss
FROM TEMP
GROUP BY stock_name