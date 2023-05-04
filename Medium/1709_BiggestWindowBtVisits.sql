-- Assume today's date is '2021-1-1'.
-- Write an SQL query that will, for each user_id, find out the largest window of days between each visit and the one right after it (or today if you are considering the last visit).
-- Return the result table ordered by user_id.
with new_date as (
    select distinct user_id,
        '2021-1-1' as visit_date
    from UserVisits
    union
    select *
    from UserVisits
),
windows as (
    select user_id,
        datediff(
            visit_date,
            lag(visit_date) over (
                partition by user_id
                order by visit_date
            )
        ) as win
    from new_date
)
select user_id,
    max(win) as biggest_window
from windows
group by user_id