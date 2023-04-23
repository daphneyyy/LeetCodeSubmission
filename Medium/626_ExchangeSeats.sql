-- Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.
select (
        case
            when id % 2 = 1
            and id + 1 <= (
                select count(*)
                from Seat
            ) then id + 1
            when id % 2 = 1 then id
            else id - 1
        end
    ) as id,
    student
from Seat
order by id