-- A quiet student is the one who took at least one exam and did not score the high or the low score.
-- Write an SQL query to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.
-- Return the result table ordered by student_id.
with tempA as(
    select *,
        rank() over (
            partition by exam_id
            order by score desc
        ) as rk
    from exam
),
tempB as (
    select *,
        max(rk) over (partition by exam_id) as cnt
    from tempA
)
select distinct s.student_id,
    s.student_name
from tempB t
    left join student s on t.student_id = s.student_id
where t.student_id not in (
        select student_id
        from tempB
        where rk = 1
            or rk = cnt
    )
order by s.student_id;