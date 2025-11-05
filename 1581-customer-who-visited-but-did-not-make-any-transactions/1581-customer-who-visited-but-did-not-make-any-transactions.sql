# Write your MySQL query statement below
SELECT v.customer_id, count(v.visit_id) as count_no_trans
FROM Visits as v
    LEFT JOIN (SELECT visit_id, coalesce(amount, 0) as amount
               FROM Transactions) as t ON v.visit_id = t.visit_id
WHERE (t.amount) IS NULL
GROUP BY v.customer_id