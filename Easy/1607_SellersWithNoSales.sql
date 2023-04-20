-- Write an SQL query to report the names of all sellers who did not make any sales in 2020.

-- Return the result table ordered by seller_name in ascending order.


select s.seller_name
from Seller s
where s.seller_id not in (
  select o.seller_id
  from Orders o
  where left(o.sale_date, 4) = "2020"
)
order by s.seller_name;