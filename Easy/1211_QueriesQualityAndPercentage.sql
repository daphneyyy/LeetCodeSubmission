-- We define query quality as:
-- The average of the ratio between query rating and its position.
-- We also define poor query percentage as:
-- The percentage of all queries with rating less than 3.
-- Write an SQL query to find each query_name, the quality and poor_query_percentage.
-- Both quality and poor_query_percentage should be rounded to 2 decimal places.
-- Return the result table in any order.
select query_name,
    round(avg(rating / position), 2) as quality,
    round(avg(rating < 3) * 100, 2) as poor_query_percentage
from Queries
group by query_name;