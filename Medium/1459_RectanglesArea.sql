-- Write an SQL query to report all possible axis-aligned rectangles with a non-zero area that can be formed by any two points from the Points table.
-- Each row in the result should contain three columns (p1, p2, area) where:
-- p1 and p2 are the id's of the two points that determine the opposite corners of a rectangle.
-- area is the area of the rectangle and must be non-zero.
-- Return the result table ordered by area in descending order. If there is a tie, order them by p1 in ascending order. If there is still a tie, order them by p2 in ascending order.
select a.id as P1,
    b.id as P2,
    abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) as AREA
from Points a,
    Points b
where a.id != b.id
    and a.id < b.id
    and a.x_value != b.x_value
    and a.y_value != b.y_value
order by area desc,
    P1,
    P2