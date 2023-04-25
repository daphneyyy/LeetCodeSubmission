-- Write an SQL query to find the most recent order(s) of each product.
-- Return the result table ordered by product_name in ascending order and in case of a tie by the product_id in ascending order. If there still a tie, order them by order_id in ascending order.
with recent_date as (
    select o.product_id,
        p.product_name,
        max(o.order_date) as order_date
    from Orders o,
        Products p
    where o.product_id = p.product_id
    group by p.product_id
)
select r.product_name,
    r.product_id,
    o.order_id,
    o.order_date
from recent_date r,
    Orders o
where r.product_id = o.product_id
    and r.order_date = o.order_date
order by r.product_name,
    r.product_id,
    o.order_id