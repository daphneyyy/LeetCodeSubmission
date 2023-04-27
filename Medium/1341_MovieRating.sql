-- Write an SQL query to:
-- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
with ratings_count as (
    select b.name as results
    from MovieRating a
        join Users b on a.user_id = b.user_id
    group by b.user_id,
        b.name
    order by count(a.movie_id) desc,
        results
    limit 1
), ratings_avg as (
    select b.title as results
    from MovieRating a
        join Movies b on a.movie_id = b.movie_id
        and left(a.created_at, 7) = '2020-02'
    group by b.movie_id,
        b.title
    order by avg(a.rating) desc,
        results
    limit 1
)
select *
from ratings_count
union
select *
from ratings_avg;