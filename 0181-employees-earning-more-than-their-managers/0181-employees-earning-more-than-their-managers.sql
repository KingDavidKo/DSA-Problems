/* Write your PL/SQL query statement below */
select name as Employee
from Employee e1
where managerId is not NULL 
and e1.salary > (select e2.salary from Employee e2 where e2.id = e1.managerId);