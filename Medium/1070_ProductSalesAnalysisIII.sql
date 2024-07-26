-- Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

-- Return the resulting table in any order.

select product_id, year as first_year, quantity, price
from sales
where (product_id, year) in (
    select product_id, min(year)
    from sales
    group by product_id
)
