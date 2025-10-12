/* Write your PL/SQL query statement below */
select name
from SalesPerson
where SalesPerson.sales_id not in (
    select Orders.sales_id
    from Company, Orders
    where Company.name = 'RED' and Orders.com_id = Company.com_id); 