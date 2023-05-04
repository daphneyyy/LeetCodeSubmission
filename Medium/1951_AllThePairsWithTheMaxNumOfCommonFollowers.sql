-- Write an SQL query to find all the pairs of users with the maximum number of common followers. In other words, if the maximum number of common followers between any two users is maxCommon, then you have to return all pairs of users that have maxCommon common followers.
-- The result table should contain the pairs user1_id and user2_id where user1_id < user2_id.
-- Return the result table in any order.
with max_cnt as (
    select a.user_id as user1_id,
        b.user_id as user2_id,
        count(*) as cnt
    from Relations a,
        Relations b
    where a.user_id < b.user_id
        and a.follower_id = b.follower_id
    group by a.user_id,
        b.user_id
)
select user1_id,
    user2_id
from max_cnt
where cnt = (
        select max(cnt)
        from max_cnt
    )