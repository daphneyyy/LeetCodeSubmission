-- Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

-- Return the resulting table in any order.

-- The result format is in the following example.

select p.product_name, s.year, s.price
from Sales s, Product p
where s.product_id = p.product_id
