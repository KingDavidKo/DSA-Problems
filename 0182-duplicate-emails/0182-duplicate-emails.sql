/* Write your PL/SQL query statement below */

select distinct email as EMAIL
from Person p1
where email is not NULL 
and exists 
    (select email
    from Person p2
    where p1.email = p2.email and p1.id != p2.id
    )
;