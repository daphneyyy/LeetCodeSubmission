-- Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.
-- The indirect relation between managers will not exceed three managers as the company is small.
-- Return the result table in any order.
with ids as (
    select b.employee_id as idsA,
        c.employee_id as idsB,
        d.employee_id as idsC
    from employees a
        left join employees b on b.manager_id = a.employee_id
        left join employees c on c.manager_id = b.employee_id
        left join employees d on d.manager_id = c.employee_id
    where a.employee_id = 1
        and (
            b.employee_id != 1
            or b.employee_id is null
        )
        and (
            c.employee_id != 1
            or c.employee_id is null
        )
        and (
            d.employee_id != 1
            or d.employee_id is null
        )
)
select idsA as employee_id
from ids
where idsA is not null
union
select idsB as employee_id
from ids
where idsB is not null
union
select idsC as employee_id
from ids
where idsC is not null