/* Write your PL/SQL query statement below */
select distinct num as ConsecutiveNums
from Logs l1
where (select num
    from Logs l2
    where l2.id = l1.id + 1
    ) = l1.num 
    and (select num
    from Logs l3
    where l3.id = l1.id + 2
    ) = l1.num;