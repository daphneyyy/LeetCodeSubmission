-- For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
-- Write an SQL query to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.
-- Return the result table ordered by employee_id.
select e1.employee_id,
    e1.name,
    count(e2.employee_id) as reports_count,
    round(avg(e2.age), 0) as average_age
from Employees e1,
    Employees e2
where e1.employee_id = e2.reports_to
group by e1.employee_id
order by e1.employee_id;