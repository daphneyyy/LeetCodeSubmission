-- Write an SQL query to report the device that is first logged in for each player.

-- Return the result table in any order.

select player_id, device_id
from Activity
where (player_id, event_date) in (
  select player_id, min(event_date) as first_login
  from Activity
  group by player_id
)
