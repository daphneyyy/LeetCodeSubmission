-- The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to two decimal places.

-- Write a solution to find the confirmation rate of each user.

-- Return the result table in any order.

-- The result format is in the following example.
  
with confirmation_count as (
    select s.user_id, count(*) as total, sum(c.action = 'confirmed') as confirmation
    from signups s left join confirmations c
    on s.user_id = c.user_id
    group by s.user_id
)
select user_id, round(ifnull(confirmation, 0)/total,2) as confirmation_rate
from confirmation_count 
