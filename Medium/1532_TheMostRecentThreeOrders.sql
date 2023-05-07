-- Write an SQL query to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.
-- Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. If there is still a tie, order them by order_date in descending order.
select customer_name,
    customer_id,
    order_id,
    order_date
from (
        select c.name as customer_name,
            c.customer_id,
            o.order_id,
            o.order_date,
            rank() over (
                partition by c.customer_id
                order by o.order_date desc
            ) as rk
        from orders o,
            customers c
        where o.customer_id = c.customer_id
        order by c.name,
            c.customer_id,
            o.order_date desc
    ) a
where a.rk <= 3;