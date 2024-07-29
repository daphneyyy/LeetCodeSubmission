-- 602. Friend Requests II: Who Has the Most Friends

-- Write a solution to find the people who have the most friends and the most friends number.

-- The test cases are generated so that only one person has the most friends.

with ids as (
    select accepter_id as id 
    from RequestAccepted
    union all
    select requester_id as id
    from RequestAccepted
)
select id, count(id) as num
from ids
group by id
order by num desc
limit 1
