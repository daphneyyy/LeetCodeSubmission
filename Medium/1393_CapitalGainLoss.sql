-- Write an SQL query to report the Capital gain/loss for each stock.

-- The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

-- Return the result table in any order.

-- The query result format is in the following example.

with new_table as (
    select stock_name, operation_day,
    case 
        when operation = 'Buy' then -price
        when operation = 'Sell' then price
    end as modified_price
    from Stocks
)
select stock_name, sum(modified_price) as capital_gain_loss
from new_table
group by stock_name;