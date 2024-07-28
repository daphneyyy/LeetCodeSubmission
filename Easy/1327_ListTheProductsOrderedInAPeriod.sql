-- 1327. List the Products Ordered in a Period

-- Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

-- Return the result table in any order.
  
select product_name, sum(unit) as unit
from orders o left join products p
on o.product_id = p.product_id
where order_date between '2020-02-01' and '2020-02-29'
group by product_name
having sum(unit) >= 100
