-- You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).
-- Write an SQL query to compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.
-- Return result table ordered by visited_on in ascending order.
with tempA as (
    select c2.customer_id,
        c2.visited_on,
        c2.amount,
        sum(c1.amount) as amt_sum
    from Customer c1,
        Customer c2
    where date_add(c2.visited_on, interval -6 day) in (
            select c1.visited_on
            from Customer c1
        )
        and c1.visited_on between date_add(c2.visited_on, interval -6 day)
        and date_add(c2.visited_on, interval -1 day)
    group by c2.customer_id,
        c2.visited_on,
        c2.amount
),
tempB as (
    select a.visited_on,
        sum(a.amount) as amt_sum
    from tempA a
    group by a.visited_on
),
tempC as (
    select distinct visited_on,
        amt_sum
    from tempA
)
select visited_on,
    sum(amt_sum) as amount,
    round(sum(amt_sum) / 7, 2) as average_amount
from (
        select *
        from tempB
        union
        select *
        from tempC
    ) d
group by visited_on