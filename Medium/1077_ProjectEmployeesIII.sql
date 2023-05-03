-- select p.project_id, e.employee_id
select project_id,
    employee_id
from (
        select project_id,
            e.employee_id,
            rank() over (
                partition by project_id
                order by experience_years desc
            ) as rk
        from Project p,
            Employee e
        where p.employee_id = e.employee_id
    ) a
where a.rk = 1