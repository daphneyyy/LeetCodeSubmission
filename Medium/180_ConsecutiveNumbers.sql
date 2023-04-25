-- Write an SQL query to find all numbers that appear at least three times consecutively.
-- Return the result table in any order.
select a.num as ConsecutiveNums
from Logs a,
    Logs b,
    Logs c
where b.id = a.id + 1
    and c.id = b.id + 1
    and a.num = b.num
    and b.num = c.num
group by a.num;