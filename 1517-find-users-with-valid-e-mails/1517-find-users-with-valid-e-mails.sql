# Write your MySQL query statement below
SELECT *
FROM Users as u
WHERE (u.mail REGEXP '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$','c');