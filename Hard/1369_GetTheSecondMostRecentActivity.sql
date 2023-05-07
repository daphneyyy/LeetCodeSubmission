-- Write an SQL query to show the second most recent activity of each user.
-- If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.
-- Return the result table in any order.
select username,
    activity,
    startDate,
    endDate
from (
        select *,
            rank() over (
                partition by username
                order by endDate desc
            ) as rk,
            count(*) over (partition by username) as cnt
        from UserActivity
    ) a
where a.cnt = 1
    or (
        a.cnt > 1
        and a.rk = 2
    )