-- Write an SQL query to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.
select round(
        count(a.player_id) /(
            select count(distinct player_id)
            from Activity
        ),
        2
    ) as fraction
from (
        select player_id,
            min(event_date) as first_day
        from Activity
        group by player_id
    ) a
    join Activity b on a.player_id = b.player_id
    and datediff(b.event_date, a.first_day) = 1