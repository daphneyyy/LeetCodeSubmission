-- Write an SQL query to evaluate the boolean expressions in Expressions table.
-- Return the result table in any order.
with xval as (
    select e.left_operand, e.operator, e.right_operand, v.value as left_val
    from Expressions e
    left join Variables v on e.left_operand = v.name
), yval as (
    select a.left_operand, a.operator, a.right_operand, a.left_val, v.value as right_val
    from xval a
    left join Variables v on a.right_operand = v.name
)
select b.left_operand, b.operator, b.right_operand, (
    case
    when b.operator = ">" and b.left_val > b.right_val then 'true'
    when b.operator = "<" and b.left_val < b.right_val then 'true'
    when b.operator = "=" and b.left_val = b.right_val then 'true'
    else 'false'
    end
) as value
from yval b;
