# Write your MySQL query statement below
WITH TEMP AS(
    SELECT buyer_id, count(order_date) as orders_in_2019
    FROM Orders
    WHERE order_date >= '2019-01-01'
    GROUP BY buyer_id
)
SELECT u.user_id as buyer_id, u.join_date, IFNULL(t.orders_in_2019, 0) as orders_in_2019
FROM Users as u
    LEFT JOIN TEMP as t ON u.user_id = t.buyer_id
