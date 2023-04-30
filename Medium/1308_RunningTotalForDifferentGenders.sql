-- Write an SQL query to find the total score for each gender on each day.
-- Return the result table ordered by gender and day in ascending order.
select gender,
    day,
    sum(score_points) over (
        partition by gender
        order by day
    ) as total
from Scores