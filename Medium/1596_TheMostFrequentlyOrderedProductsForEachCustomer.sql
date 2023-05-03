-- Write an SQL query to find the most frequently ordered product(s) for each customer.
-- The result table should have the product_id and product_name for each customer_id who ordered at least one order.
-- Return the result table in any order.
with temp as (
    select *,
        rank() over (
            partition by customer_id
            order by cnt desc
        ) as rk
    from (
            select customer_id,
                product_id,
                count(order_id) as cnt
            from Orders
            group by customer_id,
                product_id
            order by customer_id,
                product_id
        ) a
)
select t.customer_id,
    t.product_id,
    p.product_name
from temp t,
    Products p
where t.product_id = p.product_id
    and rk = 1