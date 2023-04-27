-- You are running an e-commerce site that is looking for imbalanced orders. An imbalanced order is one whose maximum quantity is strictly greater than the average quantity of every order (including itself).
-- The average quantity of an order is calculated as (total quantity of all products in the order) / (number of different products in the order). The maximum quantity of an order is the highest quantity of any single product in the order.
-- Write an SQL query to find the order_id of all imbalanced orders.
-- Return the result table in any order.
select o.order_id
from OrdersDetails o
group by o.order_id
having max(o.quantity) > (
        select max(avg_quan)
        from (
                select o.order_id,
                    avg(o.quantity) as avg_quan
                from OrdersDetails o
                group by o.order_id
            ) a
    )