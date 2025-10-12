/* Write your PL/SQL query statement below */
DELETE Person p1
WHERE exists (
    SELECT 1
    FROM Person p2 
    WHERE p1.email = p2.email and p1.id > p2.id
);