-- Write an SQL query to find the team size of each of the employees.
-- Return result table in any order.
select e1.employee_id,
    e2.team_size
from Employee e1,
    (
        select e.team_id,
            count(e.employee_id) as team_size
        from Employee e
        group by e.team_id
    ) e2
where e1.team_id = e2.team_id;