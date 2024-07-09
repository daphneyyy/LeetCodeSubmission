-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
-- Return the result table sorted in any order.
-- The result format is in the following example.
  
select customer_id, count(*) as count_no_trans
from visits
where visit_id not in (
    select visit_id 
    from transactions
)
group by customer_id
