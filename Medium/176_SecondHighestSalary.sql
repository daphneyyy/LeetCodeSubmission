-- Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

select (
    select salary
    from employee
    group by salary
    order by salary desc limit 1,1
) as SecondHighestSalary
