/* Write your PL/SQL query statement below */

select d.name as Department, e.name as Employee, salary as Salary
from Department d, Employee e
where e.departmentId = d.id
and salary = (
    select max(salary)
    from Employee e2
    where e2.departmentId = e.departmentId 
);