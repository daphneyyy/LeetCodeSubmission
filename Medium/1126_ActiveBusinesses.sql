-- The average activity for a particular event_type is the average occurences across all companies that have this event.
-- An active business is a business that has more than one event_type such that their occurences is strictly greater than the average activity for that event.
-- Write an SQL query to find all active businesses.
-- Return the result table in any order.
with avg_act as (
    select event_type,
        avg(occurences) as avg_occ
    from Events
    group by event_type
)
select business_id
from Events e
group by business_id
having sum(
        occurences > (
            select avg_occ
            from avg_act a
            where e.event_type = a.event_type
        )
    ) > 1