-- Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department. Note that when an employee belongs to only one department, their primary column is 'N'.

-- Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

-- Return the result table in any order.

-- The result format is in the following example.


select employee_id, department_id
from employee
where primary_flag = 'Y' or employee_id in (
    select employee_id
    from employee
    group by employee_id 
    having count(department_id) = 1
)
