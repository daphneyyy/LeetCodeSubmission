-- Write an SQL query to find the account_id of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.
-- Return the result table in any order.
select distinct a.account_id
from LogInfo a,
    LogInfo b
where a.account_id = b.account_id
    and a.login between b.login and b.logout
    and a.ip_address != b.ip_address;