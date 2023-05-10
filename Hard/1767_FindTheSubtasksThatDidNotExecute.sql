-- Write an SQL query to report the IDs of the missing subtasks for each task_id.
-- Return the result table in any order.
with recursive cte (task_id, subtask_id) as (
    select task_id,
        1
    from tasks
    union all
    select task_id,
        subtask_id + 1
    from cte
        join tasks using(task_id)
    where subtask_id < subtasks_count
)
select *
from cte
where (task_id, subtask_id) not in (
        select *
        from executed
    )