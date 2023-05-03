-- Write an SQL query to find the start and end number of continuous ranges in the table Logs.
-- Return the result table ordered by start_id.
with temp as (
    select row_number() over (
            order by log_id
        ) as row_num,
        log_id
    from Logs
)
select min(log_id) as start_id,
    max(log_id) as end_id
from temp
group by (log_id - row_num);