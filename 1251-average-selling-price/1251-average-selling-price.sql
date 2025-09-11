
SELECT p.product_id, IFNULL(round(sum(price*units)/sum(units),2),0) as average_price
FROM Prices as p
    LEFT JOIN UnitsSold as u ON p.product_id = u.product_id AND u.purchase_date between start_date AND end_date
GROUP BY p.product_id