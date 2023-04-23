-- Write an SQL query to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.
with maxSal as (
    select d.id,
        max(e.salary) as maxSalary
    from Employee e,
        Department d
    where e.departmentId = d.id
    group by d.id
)
select d.name as Department,
    e.name as Employee,
    m.maxSalary as Salary
from Employee e,
    Department d,
    maxSal m
where e.departmentId = d.id
    and d.id = m.id
    and e.salary = m.maxSalary