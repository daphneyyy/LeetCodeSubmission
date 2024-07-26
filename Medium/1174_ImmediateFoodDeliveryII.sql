-- If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

-- The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

-- Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

select (
    round(
        sum(
            case when order_date = customer_pref_delivery_date then 1 else 0 end
            ) * 100 / count(*)
        , 2)
) as immediate_percentage
from delivery
where (customer_id, order_date) in (
    select customer_id, min(order_date) as order_date
    from delivery
    group by customer_id
)
