-- Write an SQL query to report the managers with at least five direct reports.
-- Return the result table in any order.
select distinct e2.name as name
from Employee e1,
    Employee e2
where e1.managerId = e2.id
group by e1.managerId
having count(e1.id) >= 5;