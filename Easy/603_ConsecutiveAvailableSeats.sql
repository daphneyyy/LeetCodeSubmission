-- Write an SQL query to report all the consecutive available seats in the cinema.
-- Return the result table ordered by seat_id in ascending order.
-- The test cases are generated so that more than two seats are consecutively available.
select distinct a.seat_id
from cinema a,
    cinema b
where abs(a.seat_id - b.seat_id) = 1
    and a.free = true
    and b.free = true
order by a.seat_id;