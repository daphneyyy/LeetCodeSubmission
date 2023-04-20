-- Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them to purchase this product.
-- Return the result table ordered by customer_id.
select distinct c.customer_id,
    c.customer_name
from Customers c
where c.customer_id in (
        select customer_id
        from Orders
        where product_name = 'A'
    )
    and c.customer_id in (
        select customer_id
        from Orders
        where product_name = 'B'
    )
    and c.customer_id not in (
        select customer_id
        from Orders
        where product_name = 'C'
    );