# Write your MySQL query statement below
SELECT *
FROM Users as u
WHERE regexp_like(mail, '^[A-Za-z]+[A-Za-z0-9_.-]*@leetcode[.]com$','c')