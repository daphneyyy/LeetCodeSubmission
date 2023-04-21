-- Write an SQL query to recommend pages to the user with user_id = 1 using the pages that your friends liked. It should not recommend pages you already liked.
-- Return result table in any order without duplicates.
select distinct l.page_id as recommended_page
from Likes l
where l.user_id in (
        select f.user1_id
        from Friendship f
        where f.user2_id = 1
        union
        select f.user2_id
        from Friendship f
        where f.user1_id = 1
    )
    and l.page_id not in (
        select a.page_id
        from Likes a
        where a.user_id = 1
    );