/* Write your PL/SQL query statement below */
SELECT max(salary) as SecondHighestSalary
FROM  employee
where salary < (
    Select max(salary)
    from employee);
