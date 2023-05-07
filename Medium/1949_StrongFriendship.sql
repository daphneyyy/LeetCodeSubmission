-- A friendship between a pair of friends x and y is strong if x and y have at least three common friends.
-- Write an SQL query to find all the strong friendships.
-- Note that the result table should not contain duplicates with user1_id < user2_id.
-- Return the result table in any order.
with temp as (
    select *
    from friendship
    union
    select user2_id as user1_id,
        user1_id as user2_id
    from friendship
)
select a.user1_id,
    b.user1_id as user2_id,
    count(a.user2_id) as common_friend
from temp a,
    temp b
where a.user1_id < b.user1_id
    and a.user2_id = b.user2_id
    and (a.user1_id, b.user1_id) in (
        select *
        from friendship
    )
group by a.user1_id,
    b.user1_id
having common_friend >= 3