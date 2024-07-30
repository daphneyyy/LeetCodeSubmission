-- 185. Department Top Three Salaries
-- A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

-- Write a solution to find the employees who are high earners in each of the departments.

-- Return the result table in any order.
  
with salary_ranks as (
    select 
        *,
        dense_rank() over (
            partition by departmentId
            order by salary desc
        ) as salary_rank
    from employee
)
select d.name as Department, s.name as Employee, salary as Salary 
from salary_ranks s join department d
on s.departmentId = d.id
where salary_rank < 4
