-- Write an SQL query to report the number of grand slam tournaments won by each player. Do not include the players who did not win any tournament.
-- Return the result table in any order.
select p.player_id,
    p.player_name,
    sum(cnt) as grand_slams_count
from (
        select c.Wimbledon as ids,
            count(c.Wimbledon) as cnt
        from Championships c
        group by c.Wimbledon
        union all
        select c.Fr_open as ids,
            count(c.Fr_open) as cnt
        from Championships c
        group by c.Fr_open
        union all
        select c.US_open as ids,
            count(c.US_open) as cnt
        from Championships c
        group by c.US_open
        union all
        select c.Au_open as ids,
            count(c.Au_open) as cnt
        from Championships c
        group by c.Au_open
    ) a,
    Players p
where a.ids = p.player_id
group by a.ids