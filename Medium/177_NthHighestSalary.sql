-- Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
    select distinct salary
    from (
            select salary,
                dense_rank() over (
                    order by salary desc
                ) as rk
            from Employee
        ) e
    where e.rk = N
);
END