/* Write your PL/SQL query statement below */
SELECT id,
CASE
    when p_id is NULL THEN 'Root'
    when id in (select p_id from Tree) THEN 'Inner'
    else 'Leaf'
END as type
FROM Tree;
