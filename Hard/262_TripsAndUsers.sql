-- The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.
-- Write a SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.
-- Return the result table in any order.
with unbanned as (
    select case
            when left(status, 9) = 'cancelled' then 1
            else 0
        end as cancelled,
        request_at
    from Trips
    where client_id not in (
            select users_id
            from Users
            where banned = 'Yes'
        )
        and driver_id not in (
            select users_id
            from Users
            where banned = 'Yes'
        )
        and request_at between '2013-10-01' and '2013-10-03'
)
select request_at as Day,
    round(sum(cancelled) / count(cancelled), 2) as 'Cancellation Rate'
from unbanned
group by request_at