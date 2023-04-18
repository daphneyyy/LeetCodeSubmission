-- Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.

-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

# Write your MySQL query statement below
select contest_id, round(count(user_id) * 100 / (select count(*) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id;

