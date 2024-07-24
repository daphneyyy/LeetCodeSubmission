-- Write a solution that will, for each user, return the number of followers.

-- Return the result table ordered by user_id in ascending order.

select user_id, count(follower_id) as followers_count
from followers
group by user_id
order by user_id
